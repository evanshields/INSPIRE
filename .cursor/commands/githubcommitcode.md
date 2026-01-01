# GitHub Commit Code Command

When the user invokes `/github_commit_code`, execute the following steps automatically:

## Execution Steps

1. **Check Git Status**
   - Run `git status` to see current changes
   - Verify git is initialized (if not, inform user)

2. **Check Remote Configuration**
   - Run `git remote -v` to check for GitHub remote
   - If no remote exists:
     - Prompt user: "No GitHub remote configured. Please provide your GitHub repository URL (e.g., https://github.com/username/repo.git)"
     - Once provided, run: `git remote add origin <repository-url>`
     - Confirm: "Remote 'origin' added successfully"

3. **Stage All Changes**
   - Run `git add -A` to stage all modified and untracked files
   - Show summary of files staged

4. **Generate Commit Message**
   - Analyze staged files to generate descriptive commit message
   - Check for:
     - HTML files → "HTML prototypes"
     - Files in USDV_Underwriting_Manual → "Underwriting manual"
     - Files in _PRDs → "PRD documentation"
     - .md files → "Documentation"
     - .json files → "Configuration"
     - .py files → "Python scripts"
   - Format: "Update project files - [categories] ([X] files)"
   - Example: "Update project files - HTML prototypes - Documentation (15 files)"

5. **Create Commit**
   - Run `git commit -m "<generated-message>"`
   - Confirm commit creation

6. **Push to GitHub**
   - Get current branch: `git branch --show-current`
   - Run `git push origin <branch-name>`
   - Confirm successful push

## Error Handling

- **No changes**: If `git diff --quiet` and `git diff --cached --quiet` both succeed, inform user: "No changes to commit. Working directory is clean."
- **Authentication issues**: If push fails due to auth, provide guidance on setting up GitHub credentials (SSH key or personal access token)
- **Merge conflicts**: If conflicts detected, report them and suggest resolution
- **Remote connection issues**: If remote exists but push fails, check connectivity and provide troubleshooting steps

## Alternative: Use Helper Scripts

If preferred, you can also execute the helper scripts:
- Windows: `scripts\github-commit.bat`
- Linux/Mac: `bash scripts/github-commit.sh`

However, it's better to execute the steps directly so you can provide real-time feedback and handle errors gracefully.

## Example Output

```
🔍 Checking git status...
📡 Remote repository: origin https://github.com/evanshields/INSPIRE.git
📦 Staging all changes...
📝 Generating commit message...
💾 Creating commit: Update project files - HTML prototypes - Documentation (15 files)
🚀 Pushing to GitHub...
✅ Successfully committed and pushed to GitHub!
```
