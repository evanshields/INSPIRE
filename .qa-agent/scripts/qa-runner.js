#!/usr/bin/env node

/**
 * INSPIRE QA Agent - Test Runner
 * 
 * Automatically runs tests for changed files based on .qa-agent.yml configuration.
 * Detects changes, selects relevant tests, and executes them in order (unit → integration → E2E).
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const yaml = require('js-yaml');

// Configuration
const CONFIG_FILE = path.join(process.cwd(), '.qa-agent.yml');
const DEFAULT_CONFIG = {
  watch: { paths: ['app/', 'components/', 'lib/'], debounce: 500 },
  execution: { order: ['unit', 'integration', 'e2e'], timeouts: {} },
  frameworks: { vitest: { command: 'npm run test' }, playwright: { command: 'npm run test:e2e' } }
};

// Load configuration
function loadConfig() {
  try {
    if (fs.existsSync(CONFIG_FILE)) {
      const fileContents = fs.readFileSync(CONFIG_FILE, 'utf8');
      return yaml.load(fileContents);
    }
    console.warn('⚠️  .qa-agent.yml not found, using default configuration');
    return DEFAULT_CONFIG;
  } catch (error) {
    console.error('❌ Error loading configuration:', error.message);
    process.exit(1);
  }
}

// Get changed files (from git or command line args)
function getChangedFiles() {
  const args = process.argv.slice(2);
  
  // If files provided as arguments
  if (args.length > 0) {
    return args.filter(arg => !arg.startsWith('--'));
  }
  
  // Otherwise, try to get from git
  try {
    const gitDiff = execSync('git diff --name-only HEAD', { encoding: 'utf8' });
    const gitStatus = execSync('git status --porcelain', { encoding: 'utf8' });
    
    const diffFiles = gitDiff.split('\n').filter(Boolean);
    const statusFiles = gitStatus.split('\n')
      .filter(line => line.trim())
      .map(line => line.substring(3).trim()); // Remove status prefix
    
    return [...new Set([...diffFiles, ...statusFiles])];
  } catch (error) {
    console.warn('⚠️  Could not detect changed files from git, provide files as arguments');
    return [];
  }
}

// Map source files to test files based on configuration
function mapFilesToTests(changedFiles, config) {
  const testFiles = new Set();
  const mapping = config.execution?.selection?.mapping || {};
  
  changedFiles.forEach(file => {
    // Check each mapping pattern
    Object.entries(mapping).forEach(([pattern, config]) => {
      const regex = new RegExp(pattern.replace(/\*\*/g, '.*').replace(/\//g, '\\/'));
      
      if (regex.test(file)) {
        const testTypes = config.test_types || config;
        const testPattern = config.test_pattern || `**/tests/**/*${path.basename(file, path.extname(file))}*.{test,spec}.{ts,tsx}`;
        
        // Convert glob pattern to regex and find matching test files
        if (fs.existsSync('tests')) {
          findTestFiles(testPattern, testTypes).forEach(testFile => testFiles.add(testFile));
        }
      }
    });
  });
  
  return Array.from(testFiles);
}

// Find test files matching pattern
function findTestFiles(pattern, types) {
  const testFiles = [];
  const testsDir = path.join(process.cwd(), 'tests');
  
  if (!fs.existsSync(testsDir)) {
    return testFiles;
  }
  
  function walkDir(dir, relativePath = '') {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    
    entries.forEach(entry => {
      const fullPath = path.join(dir, entry.name);
      const relPath = path.join(relativePath, entry.name);
      
      if (entry.isDirectory()) {
        walkDir(fullPath, relPath);
      } else if (entry.isFile()) {
        // Match test file patterns
        if (entry.name.match(/\.(test|spec)\.(ts|tsx|js|jsx)$/)) {
          // Check if it matches the type filter
          const typeMatch = types.some(type => {
            if (type === 'unit' && relPath.includes('/unit/')) return true;
            if (type === 'integration' && relPath.includes('/integration/')) return true;
            if (type === 'e2e' && (relPath.includes('/e2e/') || relPath.includes('.spec.'))) return true;
            return false;
          });
          
          if (typeMatch || types.length === 0) {
            testFiles.push(fullPath);
          }
        }
      }
    });
  }
  
  walkDir(testsDir);
  return testFiles;
}

// Run tests using framework command
function runTests(testFiles, testType, config) {
  const framework = testType === 'e2e' ? 'playwright' : 'vitest';
  const frameworkConfig = config.frameworks?.[framework];
  
  if (!frameworkConfig || !frameworkConfig.command) {
    console.warn(`⚠️  No command configured for ${framework}`);
    return { success: false, output: '' };
  }
  
  const command = frameworkConfig.command;
  
  console.log(`\n🧪 Running ${testType} tests...`);
  console.log(`   Command: ${command}`);
  if (testFiles.length > 0) {
    console.log(`   Test files: ${testFiles.length}`);
  }
  
  try {
    const output = execSync(command, { 
      encoding: 'utf8',
      stdio: 'inherit',
      cwd: process.cwd(),
      env: { ...process.env, FORCE_COLOR: '1' }
    });
    
    return { success: true, output };
  } catch (error) {
    return { success: false, output: error.stdout || error.message };
  }
}

// Main execution
function main() {
  console.log('🚀 INSPIRE QA Agent - Test Runner\n');
  
  const config = loadConfig();
  const changedFiles = getChangedFiles();
  
  if (changedFiles.length === 0) {
    console.log('ℹ️  No changed files detected. Running all tests...\n');
    // Run all tests
    const order = config.execution?.order || ['unit', 'integration', 'e2e'];
    
    order.forEach(testType => {
      runTests([], testType, config);
    });
    
    return;
  }
  
  console.log(`📝 Changed files detected: ${changedFiles.length}`);
  changedFiles.forEach(file => console.log(`   - ${file}`));
  
  // Map files to tests
  const testFiles = mapFilesToTests(changedFiles, config);
  
  if (testFiles.length === 0) {
    console.log('\n⚠️  No matching test files found for changed files.');
    console.log('   You may need to create tests or update .qa-agent.yml mapping.\n');
    return;
  }
  
  console.log(`\n🎯 Found ${testFiles.length} test file(s):`);
  testFiles.forEach(testFile => console.log(`   - ${path.relative(process.cwd(), testFile)}`));
  
  // Run tests in order
  const order = config.execution?.order || ['unit', 'integration', 'e2e'];
  const results = {};
  
  order.forEach(testType => {
    const typeTestFiles = testFiles.filter(file => {
      if (testType === 'unit' && file.includes('/unit/')) return true;
      if (testType === 'integration' && file.includes('/integration/')) return true;
      if (testType === 'e2e' && (file.includes('/e2e/') || file.includes('.spec.'))) return true;
      return false;
    });
    
    if (typeTestFiles.length > 0 || testFiles.length === 0) {
      results[testType] = runTests(typeTestFiles, testType, config);
    }
  });
  
  // Summary
  console.log('\n' + '='.repeat(60));
  console.log('📊 Test Run Summary\n');
  
  Object.entries(results).forEach(([type, result]) => {
    const status = result.success ? '✅' : '❌';
    console.log(`${status} ${type.toUpperCase()}: ${result.success ? 'PASSED' : 'FAILED'}`);
  });
  
  const allPassed = Object.values(results).every(r => r.success);
  
  if (!allPassed) {
    console.log('\n❌ Some tests failed. Run `npm run qa:debug` to analyze failures.');
    process.exit(1);
  } else {
    console.log('\n✅ All tests passed!');
  }
}

// Run if executed directly
if (require.main === module) {
  main();
}

module.exports = { loadConfig, getChangedFiles, mapFilesToTests, runTests };

