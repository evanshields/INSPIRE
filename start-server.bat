@echo off
echo Starting local server for INSPIRE HTML file...
echo.
echo Choose your server option:
echo 1. Python HTTP Server (port 8000)
echo 2. Node.js http-server (port 8000)
echo 3. Exit
echo.
set /p choice="Enter choice (1-3): "

if "%choice%"=="1" (
    echo.
    echo Starting Python HTTP Server on http://localhost:8000
    echo Open http://localhost:8000/inspire-ui-analytical.html in your browser
    echo Press Ctrl+C to stop the server
    echo.
    python -m http.server 8000
) else if "%choice%"=="2" (
    echo.
    echo Checking for http-server...
    where http-server >nul 2>&1
    if errorlevel 1 (
        echo http-server not found. Installing...
        npm install -g http-server
    )
    echo.
    echo Starting http-server on http://localhost:8000
    echo Open http://localhost:8000/inspire-ui-analytical.html in your browser
    echo Press Ctrl+C to stop the server
    echo.
    http-server -p 8000
) else (
    echo Exiting...
    exit /b
)

