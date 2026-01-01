#!/usr/bin/env node

/**
 * INSPIRE QA Agent - Test Debugger
 * 
 * Analyzes test failures, categorizes them, and attempts to auto-fix common issues.
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

// Run tests and capture output
function runTestsAndCapture() {
  try {
    const output = execSync('npm run test 2>&1', { encoding: 'utf8' });
    return { success: true, output };
  } catch (error) {
    return { success: false, output: error.stdout || error.stderr || error.message };
  }
}

// Categorize errors
function categorizeErrors(output, config) {
  const autoFix = config.auto_fix || {};
  const fixable = autoFix.fixable_errors || [];
  const unfixable = autoFix.unfixable_patterns || [];
  
  const errors = [];
  const lines = output.split('\n');
  
  lines.forEach((line, index) => {
    // Check for fixable errors
    fixable.forEach(pattern => {
      if (line.includes(pattern)) {
        errors.push({
          type: 'fixable',
          pattern,
          line: index + 1,
          content: line.trim(),
          category: categorizeErrorType(pattern)
        });
      }
    });
    
    // Check for unfixable errors
    unfixable.forEach(pattern => {
      if (line.includes(pattern)) {
        errors.push({
          type: 'unfixable',
          pattern,
          line: index + 1,
          content: line.trim(),
          category: 'requires_review'
        });
      }
    });
  });
  
  return errors;
}

// Categorize error type
function categorizeErrorType(pattern) {
  if (pattern.includes('module') || pattern.includes('Import')) return 'import';
  if (pattern.includes('Snapshot')) return 'snapshot';
  if (pattern.includes('Timeout')) return 'timeout';
  if (pattern.includes('mock') || pattern.includes('fixture')) return 'mock';
  if (pattern.includes('Type') || pattern.includes('Property')) return 'type';
  return 'unknown';
}

// Attempt to fix errors
function attemptFix(errors, config) {
  const autoFix = config.auto_fix || {};
  const maxAttempts = autoFix.max_attempts || 3;
  const actions = autoFix.actions || [];
  
  console.log(`\n🔧 Attempting to fix ${errors.length} error(s)...\n`);
  
  let fixed = 0;
  let attempts = 0;
  
  errors.forEach(error => {
    if (attempts >= maxAttempts) {
      console.log(`⚠️  Max fix attempts (${maxAttempts}) reached`);
      return;
    }
    
    if (error.type !== 'fixable') {
      console.log(`⏭️  Skipping unfixable error: ${error.pattern}`);
      return;
    }
    
    console.log(`\n🔨 Fixing: ${error.pattern}`);
    console.log(`   Location: Line ${error.line}`);
    console.log(`   Content: ${error.content.substring(0, 100)}...`);
    
    let fixedError = false;
    
    // Apply fix actions based on error category
    switch (error.category) {
      case 'import':
        fixedError = fixImportError(error, actions);
        break;
      case 'snapshot':
        fixedError = fixSnapshotError(error, actions);
        break;
      case 'timeout':
        fixedError = fixTimeoutError(error, actions);
        break;
      case 'mock':
        fixedError = fixMockError(error, actions);
        break;
      case 'type':
        fixedError = fixTypeError(error, actions);
        break;
      default:
        console.log(`   ⚠️  Unknown error category, cannot auto-fix`);
    }
    
    if (fixedError) {
      fixed++;
      attempts++;
      console.log(`   ✅ Fixed!`);
    } else {
      console.log(`   ❌ Could not auto-fix`);
    }
  });
  
  return { fixed, total: errors.length };
}

// Fix import errors
function fixImportError(error, actions) {
  if (!actions.includes('update_imports')) return false;
  
  // Try to find the file and fix the import
  // This is a simplified version - in practice, you'd parse the file and fix imports
  console.log(`   💡 Suggestion: Check import paths and ensure all dependencies are installed`);
  return false; // Return false to indicate manual fix needed
}

// Fix snapshot errors
function fixSnapshotError(error, actions) {
  if (!actions.includes('update_snapshots')) return false;
  
  try {
    console.log(`   💡 Updating snapshots...`);
    execSync('npm run test -- -u', { encoding: 'utf8', stdio: 'inherit' });
    return true;
  } catch (e) {
    return false;
  }
}

// Fix timeout errors
function fixTimeoutError(error, actions) {
  if (!actions.includes('increase_timeout')) return false;
  
  console.log(`   💡 Suggestion: Increase test timeout or optimize slow operations`);
  return false; // Manual fix needed
}

// Fix mock errors
function fixMockError(error, actions) {
  if (!actions.includes('fix_mock_setup')) return false;
  
  console.log(`   💡 Suggestion: Check mock setup in test file`);
  return false; // Manual fix needed
}

// Fix type errors
function fixTypeError(error, actions) {
  if (!actions.includes('add_missing_types')) return false;
  
  console.log(`   💡 Suggestion: Add missing TypeScript types`);
  return false; // Manual fix needed
}

// Generate diagnostics report
function generateDiagnostics(errors, fixResults) {
  const report = {
    timestamp: new Date().toISOString(),
    total_errors: errors.length,
    fixable_errors: errors.filter(e => e.type === 'fixable').length,
    unfixable_errors: errors.filter(e => e.type === 'unfixable').length,
    fixed_count: fixResults?.fixed || 0,
    errors_by_category: {},
    recommendations: []
  };
  
  // Group errors by category
  errors.forEach(error => {
    const category = error.category || 'unknown';
    if (!report.errors_by_category[category]) {
      report.errors_by_category[category] = [];
    }
    report.errors_by_category[category].push({
      pattern: error.pattern,
      line: error.line,
      content: error.content
    });
  });
  
  // Generate recommendations
  if (report.fixable_errors > 0 && report.fixed_count < report.fixable_errors) {
    report.recommendations.push('Review auto-fix suggestions and apply manual fixes where needed');
  }
  
  if (report.unfixable_errors > 0) {
    report.recommendations.push('Review unfixable errors - these may indicate logic or business rule issues');
  }
  
  if (report.errors_by_category.import?.length > 0) {
    report.recommendations.push('Check that all dependencies are installed: npm install');
  }
  
  if (report.errors_by_category.snapshot?.length > 0) {
    report.recommendations.push('Review snapshot changes and update if valid: npm run test -- -u');
  }
  
  return report;
}

// Save diagnostics report
function saveDiagnosticsReport(report, config) {
  const reportsDir = config.debugging?.artifacts_dir || 'tests/artifacts';
  const logsDir = path.join(reportsDir, 'logs');
  
  // Ensure directory exists
  if (!fs.existsSync(logsDir)) {
    fs.mkdirSync(logsDir, { recursive: true });
  }
  
  const filename = `qa-debug-${Date.now()}.json`;
  const filepath = path.join(logsDir, filename);
  
  fs.writeFileSync(filepath, JSON.stringify(report, null, 2));
  console.log(`\n📄 Diagnostics report saved: ${filepath}`);
  
  return filepath;
}

// Main execution
function main() {
  console.log('🐛 INSPIRE QA Agent - Test Debugger\n');
  
  const config = loadConfig();
  
  // Run tests to capture output
  console.log('🧪 Running tests to capture output...\n');
  const testResult = runTestsAndCapture();
  
  if (testResult.success) {
    console.log('✅ All tests passed! No debugging needed.');
    return;
  }
  
  console.log('❌ Tests failed. Analyzing errors...\n');
  
  // Categorize errors
  const errors = categorizeErrors(testResult.output, config);
  
  if (errors.length === 0) {
    console.log('⚠️  No categorized errors found. Raw output:\n');
    console.log(testResult.output);
    return;
  }
  
  console.log(`📊 Found ${errors.length} error(s):`);
  console.log(`   - Fixable: ${errors.filter(e => e.type === 'fixable').length}`);
  console.log(`   - Unfixable: ${errors.filter(e => e.type === 'unfixable').length}\n`);
  
  // Attempt to fix
  const fixResults = attemptFix(errors, config);
  
  // Generate diagnostics
  const diagnostics = generateDiagnostics(errors, fixResults);
  
  // Save report
  const reportPath = saveDiagnosticsReport(diagnostics, config);
  
  // Summary
  console.log('\n' + '='.repeat(60));
  console.log('📊 Debug Summary\n');
  console.log(`Total Errors: ${diagnostics.total_errors}`);
  console.log(`Fixable: ${diagnostics.fixable_errors}`);
  console.log(`Unfixable: ${diagnostics.unfixable_errors}`);
  console.log(`Fixed: ${fixResults?.fixed || 0}`);
  
  if (diagnostics.recommendations.length > 0) {
    console.log('\n💡 Recommendations:');
    diagnostics.recommendations.forEach(rec => console.log(`   - ${rec}`));
  }
  
  console.log(`\n📄 Full report: ${reportPath}`);
  
  // Re-run tests if any fixes were applied
  if (fixResults && fixResults.fixed > 0) {
    console.log('\n🔄 Re-running tests after fixes...\n');
    const rerunResult = runTestsAndCapture();
    
    if (rerunResult.success) {
      console.log('✅ Tests now pass after fixes!');
    } else {
      console.log('❌ Tests still failing. Manual review needed.');
      process.exit(1);
    }
  } else {
    process.exit(1);
  }
}

// Run if executed directly
if (require.main === module) {
  main();
}

module.exports = { categorizeErrors, attemptFix, generateDiagnostics };

