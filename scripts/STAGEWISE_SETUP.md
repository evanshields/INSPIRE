# Stagewise Extension Setup Guide for INSPIRE

## ⚠️ Important Note
**Stagewise only works with Next.js/React apps, NOT static HTML prototypes.**

If you're working with `inspire-ui-analytical.html` (a static HTML file), please use **Webvizio** instead. See `WEBVIZIO_SETUP.md` for setup instructions.

---

## Overview
Stagewise is a visual commenting tool that allows you to add comments directly on your HTML application's UI elements. **However, it requires a component-based framework like Next.js, React, Vue, or Angular.**

This guide is for reference only if you convert your HTML to Next.js.

## Prerequisites
- ✅ Stagewise extension installed in Cursor (you've already done this)
- Node.js installed (for running the toolbar setup command)

## Step-by-Step Setup

### Step 1: Verify Extension Installation
1. Open Cursor
2. Press `Ctrl+Shift+X` (or `Cmd+Shift+X` on Mac) to open Extensions
3. Search for "Stagewise" and confirm it's installed
4. The extension should be published by `stagewise.stagewise-vscode-extension`

### Step 2: Set Up a Local Development Server
Since your HTML file uses Tailwind via CDN, you need to serve it through a local server (Stagewise requires HTTP, not `file://` protocol).

**Option A: Using Python (if installed)**
```bash
# Navigate to your project root
cd C:\Users\evana\inspire

# Python 3
python -m http.server 8000

# Python 2 (if Python 3 not available)
python -m SimpleHTTPServer 8000
```

**Option B: Using Node.js (if installed)**
```bash
# Install a simple HTTP server globally (one-time)
npm install -g http-server

# Then run it
cd C:\Users\evana\inspire
http-server -p 8000
```

**Option C: Using VS Code Live Server Extension**
1. Install "Live Server" extension in Cursor
2. Right-click on `inspire-ui-analytical.html`
3. Select "Open with Live Server"

### Step 3: Initialize Stagewise Toolbar
1. Open Command Palette: `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. Type "Stagewise" and look for one of these commands:
   - `Stagewise: Initialize Toolbar`
   - `Stagewise: Auto setup toolbar`
   - Select the appropriate command

### Step 4: Install Stagewise Toolbar (Alternative Method)
If the command palette method doesn't work, use the CLI:

1. Open a terminal in your project root (`C:\Users\evana\inspire`)
2. Run:
```bash
npx stagewise@latest
```

This will:
- Guide you through the setup process
- Inject the Stagewise toolbar into your application
- Set up the necessary configuration

### Step 5: Open Your Application in Browser
1. Start your local server (from Step 2)
2. Open your browser and navigate to:
   - `http://localhost:8000/inspire-ui-analytical.html` (if using Python/Node server)
   - Or the URL provided by Live Server (usually `http://127.0.0.1:5500/inspire-ui-analytical.html`)

### Step 6: Connect Stagewise Toolbar to Cursor
1. Look for the Stagewise toolbar at the bottom of your browser page
2. Click on the toolbar to activate it
3. You'll be prompted to connect to an agent
4. Select **Cursor** from the available options
5. The toolbar should now be connected to your Cursor editor

### Step 7: Start Adding Visual Comments
1. **Enter Selection Mode**: Click on the Stagewise toolbar or press the selection button
2. **Select Elements**: Hover over and click on any UI element you want to comment on
3. **Add Comments**: A prompt will appear where you can:
   - Describe what you want to change
   - Add visual feedback
   - Request modifications
   - Example: "Make this button fully rounded and add a subtle hover animation"
4. **Send Feedback**: Submit your comment; Stagewise will process it and apply changes

## Troubleshooting

### Issue: Toolbar doesn't appear in browser
**Solution:**
- Ensure you're accessing via `http://localhost` (not `file://`)
- Check browser console for errors (F12)
- Try refreshing the page
- Verify the toolbar was injected correctly (check HTML source)

### Issue: Can't connect to Cursor
**Solution:**
- Ensure Cursor is running
- Check that the Stagewise extension is enabled
- Try restarting both Cursor and the browser
- Verify you selected "Cursor" as the agent in the toolbar

### Issue: Command palette doesn't show Stagewise commands
**Solution:**
- Reload Cursor window: `Ctrl+Shift+P` → "Developer: Reload Window"
- Check if extension is enabled in Extensions panel
- Try reinstalling the extension

### Issue: `npx stagewise@latest` fails
**Solution:**
- Ensure Node.js is installed: `node --version`
- Update npm: `npm install -g npm@latest`
- Try with explicit version: `npx stagewise@1.0.0` (check latest version)

## Quick Reference Commands

| Action | Command |
|--------|---------|
| Open Command Palette | `Ctrl+Shift+P` (Windows) / `Cmd+Shift+P` (Mac) |
| Open Extensions | `Ctrl+Shift+X` (Windows) / `Cmd+Shift+X` (Mac) |
| Reload Window | `Ctrl+Shift+P` → "Developer: Reload Window" |

## Next Steps

Once Stagewise is set up:
1. **Test Visual Comments**: Click on various elements in your INSPIRE app
2. **Add Feedback**: Try commenting on buttons, cards, tables, and other UI components
3. **Review Changes**: Stagewise will apply changes directly to your code
4. **Iterate**: Continue adding visual comments to refine your UI

## Additional Resources

- **Stagewise Quickstart**: https://stagewise.io/docs/quickstart
- **Using Different Agents**: https://stagewise.io/docs/advanced-usage/use-different-agents
- **Stagewise Documentation**: https://stagewise.io/docs

## Notes for INSPIRE Project

Your `inspire-ui-analytical.html` file is a standalone HTML file with:
- Tailwind CSS via CDN
- Complete INSPIRE UI prototype
- All states (empty, loading, error, populated)

Stagewise will work perfectly with this setup since it's a standard HTML file served over HTTP.

