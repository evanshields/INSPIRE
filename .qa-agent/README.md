# INSPIRE QA Agent

Autonomous Testing & Quality Assurance automation for the INSPIRE loan origination system.

## Overview

The QA Agent automatically runs tests when code changes, fixes common test failures, generates tests from PRDs, and provides comprehensive reporting.

## Quick Start

### Setup

1. Install QA Agent dependencies:
   ```bash
   cd .qa-agent/scripts
   npm install
   cd ../..
   ```

2. Ensure you have test frameworks installed:
   ```bash
   npm install -D vitest @testing-library/react @testing-library/jest-dom
   npm install -D playwright @playwright/test
   # or npm install -D cypress (if using Cypress instead of Playwright)
   ```

2. Create test configuration files:
   - `vitest.config.ts` (for unit/integration tests)
   - `playwright.config.ts` (for E2E tests)

3. Add npm scripts to `package.json`:
   ```json
   {
     "scripts": {
       "test": "vitest run",
       "test:watch": "vitest",
       "test:coverage": "vitest run --coverage",
       "test:e2e": "playwright test",
       "test:e2e:ui": "playwright test --ui",
       "qa:run": "node .qa-agent/scripts/qa-runner.js",
       "qa:debug": "node .qa-agent/scripts/qa-debugger.js",
       "qa:generate": "node .qa-agent/scripts/qa-generator.js",
       "qa:report": "node .qa-agent/scripts/qa-reporter.js"
     }
   }
   ```

4. Create test directory structure:
   ```
   tests/
   ├── unit/
   │   ├── components/
   │   ├── utils/
   │   ├── calculations/
   │   ├── types/
   │   └── mock/
   ├── integration/
   │   ├── context/
   │   └── api/
   └── e2e/
       ├── pipeline/
       ├── deals/
       └── borrowers/
   ```

## Usage

### Auto-Invocation (Recommended)

The QA Agent automatically runs tests when you save files in watched directories (`app/`, `components/`, `lib/`, `mock/`).

### Manual Commands

#### Run Tests for Changed Files
```bash
npm run qa:run
```

#### Debug Test Failures
```bash
npm run qa:debug
```

#### Generate Tests from PRDs
```bash
npm run qa:generate
```

#### Generate Comprehensive Report
```bash
npm run qa:report
```

## Configuration

All configuration is in `.qa-agent.yml`. Key sections:

### Watch Paths
Configure which directories trigger test runs:
```yaml
watch:
  paths:
    - app/
    - components/
    - lib/
```

### Test Mapping
Define how source files map to test files:
```yaml
execution:
  selection:
    mapping:
      "components/**/*.tsx":
        - unit
        - integration
```

### Coverage Thresholds
Set minimum coverage requirements:
```yaml
coverage:
  thresholds:
    statements: 80
    branches: 75
    functions: 80
    lines: 80
```

### Auto-Fix Settings
Configure which errors can be auto-fixed:
```yaml
auto_fix:
  enabled: true
  fixable_errors:
    - "Cannot find module"
    - "Snapshot mismatch"
```

## Test Organization

### Unit Tests
- Location: `tests/unit/`
- Focus: Pure functions, utilities, calculations, type validation
- Framework: Vitest
- Examples:
  - `lib/utils/format-currency.test.ts`
  - `lib/calculations/ltv.test.ts`
  - `lib/calculations/dscr.test.ts`

### Integration Tests
- Location: `tests/integration/`
- Focus: Component interactions, context providers, API integrations
- Framework: Vitest + React Testing Library
- Examples:
  - `components/pipeline/PipelineBoard.test.tsx`
  - `lib/context/app-context.test.tsx`

### E2E Tests
- Location: `tests/e2e/`
- Focus: Full user workflows, critical paths
- Framework: Playwright (or Cypress)
- Examples:
  - `tests/e2e/pipeline/create-deal.spec.ts`
  - `tests/e2e/underwriting/submit-application.spec.ts`

## INSPIRE-Specific Test Areas

### Critical Test Paths
1. **Underwriting Calculations** (`lib/calculations/`)
   - LTV calculations
   - DSCR calculations
   - Loan sizing logic
   - Rate calculations
   - LLPA calculations

2. **Pipeline Management** (`app/pipeline/`, `components/pipeline/`)
   - Deal status transitions
   - Stage validations
   - SLA tracking
   - Filter/sort logic

3. **Document Handling** (`components/documents/`, `lib/document-handling/`)
   - Document classification
   - File uploads
   - Document storage

4. **Borrower Eligibility** (`lib/eligibility/`)
   - Pre-qualification rules
   - Borrower classification
   - FICO validation

### Test Fixtures

Pre-configured test data in `tests/fixtures/`:
- `deals.json` - Sample deal data
- `borrowers.json` - Sample borrower data
- `loans.json` - Sample loan data
- `properties.json` - Sample property data

### Test Helpers

Utility functions in `tests/helpers/`:
- `calculations.ts` - LTV, DSCR calculation helpers
- `loan-sizing.ts` - Loan sizing helpers
- `pipeline.ts` - Pipeline state helpers
- `documents.ts` - Document mock helpers

## Reporting

Test reports are generated in `docs/qa-reports/`:
- `qa-report-{timestamp}.md` - Markdown report
- `qa-report-{timestamp}.json` - JSON data
- `qa-report-{timestamp}.html` - HTML report (optional)

Reports include:
- Test results summary
- Coverage metrics
- Failed test details
- Slow test identification
- Flaky test detection
- Recommendations

## CI/CD Integration

### GitHub Actions

The QA Agent integrates with GitHub Actions:
- Runs on pull requests
- Blocks merge if tests fail
- Posts PR comments with results
- Runs nightly scheduled tests

Workflow file: `.github/workflows/qa.yml` (to be created)

### Branch Protection

Configure branch protection rules:
- Require tests to pass
- Require coverage threshold (75%)
- Block direct pushes to main

## Troubleshooting

### Tests Not Running Automatically

1. Check `.qa-agent.yml` watch settings
2. Verify file paths match watch patterns
3. Check debounce delay (may be too high)
4. Ensure QA Agent scripts are executable

### Auto-Fix Not Working

1. Check `auto_fix.enabled: true` in config
2. Verify error matches `fixable_errors` patterns
3. Check `max_attempts` hasn't been exceeded
4. Review error logs in `tests/artifacts/logs/`

### Coverage Below Threshold

1. Identify untested files using coverage report
2. Generate tests for uncovered code: `npm run qa:generate`
3. Review coverage exclusions in config
4. Check file-specific thresholds

### Slow Test Performance

1. Check `performance.budgets` in config
2. Identify slow tests in report
3. Optimize slow tests or mark with `@slow` tag
4. Consider parallel execution settings

## Best Practices

1. **Write Tests First** (TDD) for critical calculations
2. **Keep Tests Fast** - Unit tests should be <100ms
3. **Test Business Logic** - Focus on underwriting rules, calculations
4. **Use Fixtures** - Don't hardcode test data
5. **Tag Tests** - Use `@critical`, `@slow`, `@integration` tags
6. **Maintain Coverage** - Keep coverage above 80%
7. **Review Reports** - Check reports after each run
8. **Fix Flaky Tests** - Don't ignore flaky test warnings

## Next Steps

1. Install test frameworks and create config files
2. Create initial test structure
3. Write tests for critical paths (calculations, pipeline)
4. Set up CI/CD integration
5. Generate tests from PRDs
6. Monitor coverage and test performance

## Support

For questions or issues:
- Review `.qa-agent.yml` configuration
- Check test artifacts in `tests/artifacts/`
- Review QA reports in `docs/qa-reports/`
- Consult PRD testing requirements sections

