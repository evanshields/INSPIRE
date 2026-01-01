#!/usr/bin/env node

/**
 * INSPIRE QA Agent - Test Generator
 * 
 * Generates test files from PRDs, templates, and coverage gaps.
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const yaml = require('js-yaml');

// Configuration
const CONFIG_FILE = path.join(process.cwd(), '.qa-agent.yml');

// Load configuration
function loadConfig() {
  try {
    if (fs.existsSync(CONFIG_FILE)) {
      const fileContents = fs.readFileSync(CONFIG_FILE, 'utf8');
      return yaml.load(fileContents);
    }
    console.error('❌ .qa-agent.yml not found');
    process.exit(1);
  } catch (error) {
    console.error('❌ Error loading configuration:', error.message);
    process.exit(1);
  }
}

// Load test template
function loadTemplate(templatePath) {
  try {
    if (fs.existsSync(templatePath)) {
      return fs.readFileSync(templatePath, 'utf8');
    }
    
    // Return default template if file doesn't exist
    return getDefaultTemplate();
  } catch (error) {
    console.warn(`⚠️  Could not load template ${templatePath}, using default`);
    return getDefaultTemplate();
  }
}

// Get default test template
function getDefaultTemplate() {
  return `import { describe, it, expect } from 'vitest';

describe('{{COMPONENT_NAME}}', () => {
  it('should work correctly', () => {
    expect(true).toBe(true);
  });
});
`;
}

// Extract test requirements from PRD
function extractTestRequirements(prdPath) {
  const content = fs.readFileSync(prdPath, 'utf8');
  const requirements = [];
  
  // Look for testing requirements sections
  const testSectionRegex = /##\s+\d+\.\d+\s+Testing\s+Requirements?/i;
  const testSectionMatch = content.match(testSectionRegex);
  
  if (testSectionMatch) {
    const startIndex = testSectionMatch.index;
    const remaining = content.substring(startIndex);
    const endIndex = remaining.indexOf('\n## ', 100); // Next section
    
    const testSection = endIndex > 0 ? remaining.substring(0, endIndex) : remaining;
    
    // Extract test lists
    const listRegex = /[-*]\s+(.+)/g;
    let match;
    
    while ((match = listRegex.exec(testSection)) !== null) {
      requirements.push(match[1].trim());
    }
  }
  
  return requirements;
}

// Find source files without tests
function findUntestedFiles(config) {
  const analyzePatterns = config.generation?.analyze_patterns || [
    'app/**/*.tsx',
    'components/**/*.tsx',
    'lib/**/*.ts'
  ];
  
  const untestedFiles = [];
  
  analyzePatterns.forEach(pattern => {
    const glob = pattern.replace(/\*\*/g, '**');
    const baseDir = pattern.split('/')[0];
    
    if (fs.existsSync(baseDir)) {
      walkDirectory(baseDir, (filePath) => {
        // Check if test file exists
        const testPath = findTestFile(filePath);
        if (!testPath || !fs.existsSync(testPath)) {
          untestedFiles.push(filePath);
        }
      });
    }
  });
  
  return untestedFiles;
}

// Walk directory recursively
function walkDirectory(dir, callback) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  
  entries.forEach(entry => {
    const fullPath = path.join(dir, entry.name);
    
    if (entry.isDirectory()) {
      if (!entry.name.startsWith('.') && entry.name !== 'node_modules') {
        walkDirectory(fullPath, callback);
      }
    } else if (entry.isFile()) {
      if (entry.name.match(/\.(ts|tsx)$/) && !entry.name.match(/\.(test|spec)\./)) {
        callback(fullPath);
      }
    }
  });
}

// Find corresponding test file
function findTestFile(sourceFile) {
  const ext = path.extname(sourceFile);
  const baseName = path.basename(sourceFile, ext);
  const dir = path.dirname(sourceFile);
  
  const testExtensions = ['.test.ts', '.test.tsx', '.spec.ts', '.spec.tsx'];
  
  for (const testExt of testExtensions) {
    const testFile = path.join(dir, baseName + testExt);
    if (fs.existsSync(testFile)) {
      return testFile;
    }
    
    // Also check in tests directory
    const relativePath = path.relative(process.cwd(), dir);
    const testDir = path.join(process.cwd(), 'tests', 'unit', relativePath);
    const testFileInTestsDir = path.join(testDir, baseName + testExt);
    if (fs.existsSync(testFileInTestsDir)) {
      return testFileInTestsDir;
    }
  }
  
  return null;
}

// Generate test file content
function generateTestContent(sourceFile, template, requirements = []) {
  const componentName = path.basename(sourceFile, path.extname(sourceFile));
  const relativePath = path.relative(process.cwd(), sourceFile);
  
  let content = template
    .replace(/{{COMPONENT_NAME}}/g, componentName)
    .replace(/{{FILE_PATH}}/g, relativePath);
  
  // Add test cases from requirements
  if (requirements.length > 0) {
    const testCases = requirements
      .slice(0, 5) // Limit to 5 test cases
      .map(req => `  it('${req}', () => {
    // TODO: Implement test for: ${req}
    expect(true).toBe(true);
  });`)
      .join('\n\n');
    
    content = content.replace(
      /it\('should work correctly'/,
      testCases || "it('should work correctly'"
    );
  }
  
  return content;
}

// Determine test directory
function determineTestDirectory(sourceFile, testType = 'unit') {
  const relativePath = path.relative(process.cwd(), sourceFile);
  const baseDir = relativePath.split(path.sep)[0];
  
  // Map source directories to test directories
  const mapping = {
    'app': 'tests/e2e',
    'components': `tests/${testType}/components`,
    'lib': `tests/${testType}/${baseDir === 'lib' ? 'lib' : baseDir}`
  };
  
  const testBaseDir = mapping[baseDir] || `tests/${testType}`;
  
  // Preserve subdirectory structure
  const subdir = path.dirname(relativePath).replace(baseDir, '').replace(/^[\/\\]/, '');
  const testDir = path.join(process.cwd(), testBaseDir, subdir);
  
  return testDir;
}

// Generate test file
function generateTestFile(sourceFile, config) {
  const testType = sourceFile.includes('app/') ? 'e2e' : 'unit';
  const templatePath = config.generation?.templates?.[testType];
  
  const template = templatePath ? loadTemplate(templatePath) : getDefaultTemplate();
  
  // Extract requirements from PRDs if available
  const requirements = [];
  const prdScenarios = config.inspire_specific?.prd_scenarios || {};
  
  Object.values(prdScenarios).forEach(prdPath => {
    if (fs.existsSync(prdPath)) {
      const reqs = extractTestRequirements(prdPath);
      requirements.push(...reqs);
    }
  });
  
  const content = generateTestContent(sourceFile, template, requirements);
  
  // Determine output directory
  const testDir = determineTestDirectory(sourceFile, testType);
  const componentName = path.basename(sourceFile, path.extname(sourceFile));
  const ext = path.extname(sourceFile);
  const testExt = ext === '.tsx' ? '.test.tsx' : '.test.ts';
  const testFile = path.join(testDir, componentName + testExt);
  
  // Create directory if it doesn't exist
  if (!fs.existsSync(testDir)) {
    fs.mkdirSync(testDir, { recursive: true });
  }
  
  // Write test file
  fs.writeFileSync(testFile, content, 'utf8');
  
  return testFile;
}

// Main execution
function main() {
  console.log('✨ INSPIRE QA Agent - Test Generator\n');
  
  const config = loadConfig();
  const generation = config.generation || {};
  
  if (!generation.enabled) {
    console.log('⚠️  Test generation is disabled in .qa-agent.yml');
    return;
  }
  
  const args = process.argv.slice(2);
  let filesToGenerate = [];
  
  // If files provided as arguments
  if (args.length > 0 && !args.includes('--all')) {
    filesToGenerate = args.filter(arg => !arg.startsWith('--'));
  } else {
    // Find untested files
    console.log('🔍 Finding untested files...\n');
    filesToGenerate = findUntestedFiles(config);
  }
  
  if (filesToGenerate.length === 0) {
    console.log('✅ All files have tests!');
    return;
  }
  
  console.log(`📝 Found ${filesToGenerate.length} file(s) without tests:\n`);
  filesToGenerate.slice(0, 10).forEach(file => {
    console.log(`   - ${path.relative(process.cwd(), file)}`);
  });
  
  if (filesToGenerate.length > 10) {
    console.log(`   ... and ${filesToGenerate.length - 10} more`);
  }
  
  // Generate tests
  console.log('\n🔨 Generating test files...\n');
  
  const generated = [];
  const failed = [];
  
  filesToGenerate.slice(0, 20).forEach(sourceFile => { // Limit to 20 at a time
    try {
      const testFile = generateTestFile(sourceFile, config);
      generated.push(testFile);
      console.log(`✅ Generated: ${path.relative(process.cwd(), testFile)}`);
    } catch (error) {
      failed.push({ file: sourceFile, error: error.message });
      console.log(`❌ Failed: ${path.relative(process.cwd(), sourceFile)} - ${error.message}`);
    }
  });
  
  // Summary
  console.log('\n' + '='.repeat(60));
  console.log('📊 Generation Summary\n');
  console.log(`Generated: ${generated.length}`);
  console.log(`Failed: ${failed.length}`);
  
  if (generated.length > 0) {
    console.log('\n✅ Successfully generated test files:');
    generated.forEach(file => {
      console.log(`   - ${path.relative(process.cwd(), file)}`);
    });
  }
  
  if (failed.length > 0) {
    console.log('\n❌ Failed to generate:');
    failed.forEach(({ file, error }) => {
      console.log(`   - ${path.relative(process.cwd(), file)}: ${error}`);
    });
  }
  
  if (generated.length > 0) {
    console.log('\n💡 Next steps:');
    console.log('   1. Review generated test files');
    console.log('   2. Implement test logic');
    console.log('   3. Run tests: npm run test');
  }
}

// Run if executed directly
if (require.main === module) {
  main();
}

module.exports = { loadTemplate, extractTestRequirements, generateTestFile, findUntestedFiles };

