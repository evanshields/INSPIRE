#!/bin/bash

# GitHub Commit Code Script
# Automatically stages, commits, and pushes all changes to GitHub

set -e  # Exit on error

echo "🔍 Checking git status..."
git status --short

# Check if git is initialized
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Git is not initialized in this directory."
    echo "Please run: git init"
    exit 1
fi

# Check if remote is configured
if ! git remote | grep -q "origin"; then
    echo "⚠️  No GitHub remote configured."
    read -p "Enter GitHub repository URL (e.g., https://github.com/username/repo.git): " repo_url
    if [ -z "$repo_url" ]; then
        echo "❌ No URL provided. Exiting."
        exit 1
    fi
    git remote add origin "$repo_url"
    echo "✅ Remote 'origin' added: $repo_url"
fi

# Show remote URL
echo "📡 Remote repository:"
git remote -v | grep origin

# Check if there are changes to commit
if git diff --quiet && git diff --cached --quiet; then
    echo "✅ No changes to commit. Working directory is clean."
    exit 0
fi

# Stage all changes
echo "📦 Staging all changes..."
git add -A

# Generate commit message based on changes
echo "📝 Generating commit message..."
changed_files=$(git diff --cached --name-only)

# Analyze file types
html_count=$(echo "$changed_files" | grep -c "\.html$" || true)
md_count=$(echo "$changed_files" | grep -c "\.md$" || true)
json_count=$(echo "$changed_files" | grep -c "\.json$" || true)
py_count=$(echo "$changed_files" | grep -c "\.py$" || true)
total_count=$(echo "$changed_files" | wc -l | tr -d ' ')

# Build commit message
commit_msg="Update project files"

if [ "$html_count" -gt 0 ]; then
    commit_msg="$commit_msg - HTML prototypes"
fi

if echo "$changed_files" | grep -q "underwriting\|USDV_Underwriting_Manual"; then
    commit_msg="$commit_msg - Underwriting manual"
fi

if echo "$changed_files" | grep -q "PRD\|prd"; then
    commit_msg="$commit_msg - PRD documentation"
fi

if [ "$md_count" -gt 0 ]; then
    commit_msg="$commit_msg - Documentation"
fi

if [ "$json_count" -gt 0 ]; then
    commit_msg="$commit_msg - Configuration"
fi

if [ "$py_count" -gt 0 ]; then
    commit_msg="$commit_msg - Python scripts"
fi

commit_msg="$commit_msg ($total_count files)"

# Create commit
echo "💾 Creating commit: $commit_msg"
git commit -m "$commit_msg"

# Get current branch
current_branch=$(git branch --show-current)

# Push to remote
echo "🚀 Pushing to GitHub..."
git push origin "$current_branch"

echo "✅ Successfully committed and pushed to GitHub!"
echo "📊 Commit: $commit_msg"
echo "🌿 Branch: $current_branch"

