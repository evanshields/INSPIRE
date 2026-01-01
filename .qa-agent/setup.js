#!/usr/bin/env node

/**
 * INSPIRE QA Agent Setup Script
 * 
 * Installs dependencies and sets up the QA Agent environment.
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

console.log('🚀 INSPIRE QA Agent Setup\n');

// Install QA Agent script dependencies
console.log('📦 Installing QA Agent dependencies...');
try {
  const scriptsDir = path.join(__dirname, 'scripts');
  process.chdir(scriptsDir);
  execSync('npm install', { stdio: 'inherit' });
  console.log('✅ QA Agent dependencies installed\n');
} catch (error) {
  console.error('❌ Failed to install QA Agent dependencies:', error.message);
  console.log('\n💡 Try running manually: cd .qa-agent/scripts && npm install\n');
}

// Check for .qa-agent.yml
const projectRoot = path.join(__dirname, '..');
process.chdir(projectRoot);

if (!fs.existsSync('.qa-agent.yml')) {
  console.log('⚠️  .qa-agent.yml not found in project root');
  console.log('   Please ensure the configuration file exists.\n');
} else {
  console.log('✅ .qa-agent.yml found\n');
}

// Create test directories if they don't exist
const testDirs = [
  'tests/unit',
  'tests/integration',
  'tests/e2e',
  'tests/fixtures',
  'tests/helpers',
  'tests/artifacts/logs',
  'tests/artifacts/screenshots',
  'tests/artifacts/videos',
  'docs/qa-reports'
];

console.log('📁 Creating test directory structure...');
testDirs.forEach(dir => {
  const fullPath = path.join(projectRoot, dir);
  if (!fs.existsSync(fullPath)) {
    fs.mkdirSync(fullPath, { recursive: true });
    console.log(`   ✅ Created: ${dir}`);
  } else {
    console.log(`   ℹ️  Exists: ${dir}`);
  }
});
console.log('');

// Check for test framework installations
console.log('🔍 Checking test framework installations...\n');

const packageJsonPath = path.join(projectRoot, 'package.json');
if (fs.existsSync(packageJsonPath)) {
  const packageJson = JSON.parse(fs.readFileSync(packageJsonPath, 'utf8'));
  const devDeps = packageJson.devDependencies || {};
  
  const requiredPackages = {
    'vitest': 'Vitest (unit/integration tests)',
    '@testing-library/react': 'React Testing Library',
    '@playwright/test': 'Playwright (E2E tests)'
  };
  
  Object.entries(requiredPackages).forEach(([pkg, description]) => {
    if (devDeps[pkg] || packageJson.dependencies?.[pkg]) {
      console.log(`   ✅ ${pkg} - ${description}`);
    } else {
      console.log(`   ⚠️  ${pkg} - ${description} (not installed)`);
      console.log(`      Install: npm install -D ${pkg}`);
    }
  });
} else {
  console.log('   ⚠️  package.json not found');
  console.log('   Create package.json and install test frameworks\n');
}

console.log('\n' + '='.repeat(60));
console.log('✨ Setup Complete!\n');
console.log('Next steps:');
console.log('1. Install test frameworks if missing (see above)');
console.log('2. Create vitest.config.ts and playwright.config.ts');
console.log('3. Add npm scripts to package.json (see README.md)');
console.log('4. Run: npm run qa:run\n');

