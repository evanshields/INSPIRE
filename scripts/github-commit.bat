@echo off
REM GitHub Commit Code Script for Windows
REM Automatically stages, commits, and pushes all changes to GitHub

echo Checking git status...
git status --short

REM Check if git is initialized
git rev-parse --git-dir >nul 2>&1
if errorlevel 1 (
    echo Git is not initialized in this directory.
    echo Please run: git init
    exit /b 1
)

REM Check if remote is configured
git remote | findstr /C:"origin" >nul 2>&1
if errorlevel 1 (
    echo No GitHub remote configured.
    set /p repo_url="Enter GitHub repository URL (e.g., https://github.com/username/repo.git): "
    if "!repo_url!"=="" (
        echo No URL provided. Exiting.
        exit /b 1
    )
    git remote add origin "!repo_url!"
    echo Remote 'origin' added: !repo_url!
)

REM Show remote URL
echo Remote repository:
git remote -v | findstr "origin"

REM Check if there are changes to commit
git diff --quiet >nul 2>&1
set has_unstaged=%errorlevel%
git diff --cached --quiet >nul 2>&1
set has_staged=%errorlevel%

if %has_unstaged%==0 if %has_staged%==0 (
    echo No changes to commit. Working directory is clean.
    exit /b 0
)

REM Stage all changes
echo Staging all changes...
git add -A

REM Generate commit message
echo Generating commit message...
for /f "delims=" %%f in ('git diff --cached --name-only') do set changed_files=%%f

REM Count file types (simplified for Windows batch)
set html_count=0
set md_count=0
set json_count=0
set py_count=0
set total_count=0

for /f "delims=" %%f in ('git diff --cached --name-only') do (
    set /a total_count+=1
    echo %%f | findstr /R "\.html$" >nul && set /a html_count+=1
    echo %%f | findstr /R "\.md$" >nul && set /a md_count+=1
    echo %%f | findstr /R "\.json$" >nul && set /a json_count+=1
    echo %%f | findstr /R "\.py$" >nul && set /a py_count+=1
)

REM Build commit message
set commit_msg=Update project files

if %html_count% gtr 0 set commit_msg=%commit_msg% - HTML prototypes

echo %changed_files% | findstr /I "underwriting USDV_Underwriting_Manual" >nul
if not errorlevel 1 set commit_msg=%commit_msg% - Underwriting manual

echo %changed_files% | findstr /I "PRD prd" >nul
if not errorlevel 1 set commit_msg=%commit_msg% - PRD documentation

if %md_count% gtr 0 set commit_msg=%commit_msg% - Documentation
if %json_count% gtr 0 set commit_msg=%commit_msg% - Configuration
if %py_count% gtr 0 set commit_msg=%commit_msg% - Python scripts

set commit_msg=%commit_msg% (%total_count% files)

REM Create commit
echo Creating commit: %commit_msg%
git commit -m "%commit_msg%"

REM Get current branch
for /f "delims=" %%b in ('git branch --show-current') do set current_branch=%%b

REM Push to remote
echo Pushing to GitHub...
git push origin %current_branch%

echo Successfully committed and pushed to GitHub!
echo Commit: %commit_msg%
echo Branch: %current_branch%

