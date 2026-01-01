#!/usr/bin/env node

/**
 * INSPIRE QA Agent - Test Reporter
 * 
 * Generates comprehensive test reports in multiple formats (Markdown, JSON, HTML).
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

// Run tests and collect coverage
function collectTestResults(config) {
  console.log('🧪 Running tests and collecting results...\n');
  
  const results = {
    unit: { passed: 0, failed: 0, skipped: 0, duration: 0 },
    integration: { passed: 0, failed: 0, skipped: 0, duration: 0 },
    e2e: { passed: 0, failed: 0, skipped: 0, duration: 0 }
  };
  
  // Run unit/integration tests (Vitest)
  try {
    const vitestOutput = execSync('npm run test:coverage 2>&1', { encoding: 'utf8' });
    parseVitestOutput(vitestOutput, results);
  } catch (error) {
    parseVitestOutput(error.stdout || error.stderr || '', results);
  }
  
  // Run E2E tests (Playwright)
  try {
    const playwrightOutput = execSync('npm run test:e2e -- --reporter=json 2>&1', { encoding: 'utf8' });
    parsePlaywrightOutput(playwrightOutput, results);
  } catch (error) {
    // E2E tests may not be configured yet
    console.log('⚠️  E2E tests not available');
  }
  
  return results;
}

// Parse Vitest output
function parseVitestOutput(output, results) {
  // Simple parsing - in practice, use JSON reporter
  const passedMatch = output.match(/(\d+)\s+passed/);
  const failedMatch = output.match(/(\d+)\s+failed/);
  const skippedMatch = output.match(/(\d+)\s+skipped/);
  
  if (passedMatch) results.unit.passed = parseInt(passedMatch[1]);
  if (failedMatch) results.unit.failed = parseInt(failedMatch[1]);
  if (skippedMatch) results.unit.skipped = parseInt(skippedMatch[1]);
  
  // Try to parse duration
  const durationMatch = output.match(/Time:\s+([\d.]+)\s*s/);
  if (durationMatch) results.unit.duration = parseFloat(durationMatch[1]) * 1000;
}

// Parse Playwright output
function parsePlaywrightOutput(output, results) {
  try {
    const jsonMatch = output.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      const json = JSON.parse(jsonMatch[0]);
      if (json.stats) {
        results.e2e.passed = json.stats.expected || 0;
        results.e2e.failed = json.stats.unexpected || 0;
        results.e2e.skipped = json.stats.skipped || 0;
        results.e2e.duration = json.stats.duration || 0;
      }
    }
  } catch (error) {
    // Fallback parsing
    const passedMatch = output.match(/(\d+)\s+passed/);
    const failedMatch = output.match(/(\d+)\s+failed/);
    if (passedMatch) results.e2e.passed = parseInt(passedMatch[1]);
    if (failedMatch) results.e2e.failed = parseInt(failedMatch[1]);
  }
}

// Get coverage data
function getCoverageData() {
  try {
    const coveragePath = path.join(process.cwd(), 'coverage', 'coverage-summary.json');
    if (fs.existsSync(coveragePath)) {
      return JSON.parse(fs.readFileSync(coveragePath, 'utf8'));
    }
  } catch (error) {
    console.warn('⚠️  Could not load coverage data');
  }
  return null;
}

// Calculate metrics
function calculateMetrics(results, coverage) {
  const total = {
    passed: results.unit.passed + results.integration.passed + results.e2e.passed,
    failed: results.unit.failed + results.integration.failed + results.e2e.failed,
    skipped: results.unit.skipped + results.integration.skipped + results.e2e.skipped,
    duration: results.unit.duration + results.integration.duration + results.e2e.duration
  };
  
  total.total = total.passed + total.failed + total.skipped;
  total.passRate = total.total > 0 ? (total.passed / total.total * 100).toFixed(2) : 0;
  
  const metrics = {
    totals: total,
    by_type: results,
    coverage: coverage ? {
      statements: coverage.total?.statements?.pct || 0,
      branches: coverage.total?.branches?.pct || 0,
      functions: coverage.total?.functions?.pct || 0,
      lines: coverage.total?.lines?.pct || 0
    } : null,
    timestamp: new Date().toISOString()
  };
  
  return metrics;
}

// Generate Markdown report
function generateMarkdownReport(metrics, config) {
  const report = `# INSPIRE QA Test Report

**Generated:** ${new Date(metrics.timestamp).toLocaleString()}

---

## Summary

| Metric | Value |
|--------|-------|
| **Total Tests** | ${metrics.totals.total} |
| **Passed** | ${metrics.totals.passed} ✅ |
| **Failed** | ${metrics.totals.failed} ${metrics.totals.failed > 0 ? '❌' : ''} |
| **Skipped** | ${metrics.totals.skipped} |
| **Pass Rate** | ${metrics.totals.passRate}% |
| **Duration** | ${(metrics.totals.duration / 1000).toFixed(2)}s |

---

## Results by Type

### Unit Tests
- ✅ Passed: ${metrics.by_type.unit.passed}
- ❌ Failed: ${metrics.by_type.unit.failed}
- ⏭️ Skipped: ${metrics.by_type.unit.skipped}
- ⏱️ Duration: ${(metrics.by_type.unit.duration / 1000).toFixed(2)}s

### Integration Tests
- ✅ Passed: ${metrics.by_type.integration.passed}
- ❌ Failed: ${metrics.by_type.integration.failed}
- ⏭️ Skipped: ${metrics.by_type.integration.skipped}
- ⏱️ Duration: ${(metrics.by_type.integration.duration / 1000).toFixed(2)}s

### E2E Tests
- ✅ Passed: ${metrics.by_type.e2e.passed}
- ❌ Failed: ${metrics.by_type.e2e.failed}
- ⏭️ Skipped: ${metrics.by_type.e2e.skipped}
- ⏱️ Duration: ${(metrics.by_type.e2e.duration / 1000).toFixed(2)}s

---

${metrics.coverage ? `## Code Coverage

| Metric | Coverage | Status |
|--------|----------|--------|
| **Statements** | ${metrics.coverage.statements}% | ${metrics.coverage.statements >= 80 ? '✅' : '⚠️'} |
| **Branches** | ${metrics.coverage.branches}% | ${metrics.coverage.branches >= 75 ? '✅' : '⚠️'} |
| **Functions** | ${metrics.coverage.functions}% | ${metrics.coverage.functions >= 80 ? '✅' : '⚠️'} |
| **Lines** | ${metrics.coverage.lines}% | ${metrics.coverage.lines >= 80 ? '✅' : '⚠️'} |

---

` : ''}## Recommendations

${generateRecommendations(metrics, config)}

---

*Report generated by INSPIRE QA Agent*
`;

  return report;
}

// Generate recommendations
function generateRecommendations(metrics, config) {
  const recommendations = [];
  
  if (metrics.totals.failed > 0) {
    recommendations.push(`- Fix ${metrics.totals.failed} failing test(s): Run \`npm run qa:debug\` to analyze failures`);
  }
  
  if (metrics.coverage) {
    const thresholds = config.coverage?.thresholds || {};
    
    if (metrics.coverage.statements < (thresholds.statements || 80)) {
      recommendations.push(`- Improve statement coverage (currently ${metrics.coverage.statements}%, target: ${thresholds.statements || 80}%)`);
    }
    
    if (metrics.coverage.branches < (thresholds.branches || 75)) {
      recommendations.push(`- Improve branch coverage (currently ${metrics.coverage.branches}%, target: ${thresholds.branches || 75}%)`);
    }
  }
  
  if (metrics.totals.passRate < 90) {
    recommendations.push(`- Improve overall pass rate (currently ${metrics.totals.passRate}%)`);
  }
  
  if (recommendations.length === 0) {
    recommendations.push('- ✅ All metrics are within acceptable ranges!');
  }
  
  return recommendations.join('\n');
}

// Save report
function saveReport(content, format, config) {
  const outputDir = config.reporting?.output_dir || 'docs/qa-reports';
  
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, -5);
  const extension = format === 'json' ? 'json' : format === 'html' ? 'html' : 'md';
  const filename = `qa-report-${timestamp}.${extension}`;
  const filepath = path.join(outputDir, filename);
  
  fs.writeFileSync(filepath, content, 'utf8');
  
  return filepath;
}

// Main execution
function main() {
  console.log('📊 INSPIRE QA Agent - Test Reporter\n');
  
  const config = loadConfig();
  const reporting = config.reporting || {};
  const formats = reporting.formats || ['markdown', 'json'];
  
  // Collect test results
  const results = collectTestResults(config);
  
  // Get coverage data
  const coverage = getCoverageData();
  
  // Calculate metrics
  const metrics = calculateMetrics(results, coverage);
  
  // Generate reports
  const savedReports = [];
  
  if (formats.includes('markdown')) {
    const markdown = generateMarkdownReport(metrics, config);
    const filepath = saveReport(markdown, 'markdown', config);
    savedReports.push(filepath);
    console.log(`✅ Markdown report: ${filepath}`);
  }
  
  if (formats.includes('json')) {
    const json = JSON.stringify(metrics, null, 2);
    const filepath = saveReport(json, 'json', config);
    savedReports.push(filepath);
    console.log(`✅ JSON report: ${filepath}`);
  }
  
  if (formats.includes('html')) {
    // HTML generation would go here
    console.log('⚠️  HTML format not yet implemented');
  }
  
  // Print summary
  console.log('\n' + '='.repeat(60));
  console.log('📊 Report Summary\n');
  console.log(`Total Tests: ${metrics.totals.total}`);
  console.log(`Passed: ${metrics.totals.passed} ✅`);
  console.log(`Failed: ${metrics.totals.failed} ${metrics.totals.failed > 0 ? '❌' : ''}`);
  console.log(`Pass Rate: ${metrics.totals.passRate}%`);
  
  if (metrics.coverage) {
    console.log(`\nCoverage:`);
    console.log(`  Statements: ${metrics.coverage.statements}%`);
    console.log(`  Branches: ${metrics.coverage.branches}%`);
    console.log(`  Functions: ${metrics.coverage.functions}%`);
    console.log(`  Lines: ${metrics.coverage.lines}%`);
  }
  
  console.log(`\n📄 Reports saved:`);
  savedReports.forEach(report => console.log(`   - ${report}`));
}

// Run if executed directly
if (require.main === module) {
  main();
}

module.exports = { collectTestResults, calculateMetrics, generateMarkdownReport };

