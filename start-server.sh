#!/bin/bash

echo "Starting local server for INSPIRE HTML file..."
echo ""
echo "Choose your server option:"
echo "1. Python HTTP Server (port 8000)"
echo "2. Node.js http-server (port 8000)"
echo "3. Exit"
echo ""
read -p "Enter choice (1-3): " choice

case $choice in
    1)
        echo ""
        echo "Starting Python HTTP Server on http://localhost:8000"
        echo "Open http://localhost:8000/inspire-ui-analytical.html in your browser"
        echo "Press Ctrl+C to stop the server"
        echo ""
        python3 -m http.server 8000
        ;;
    2)
        echo ""
        echo "Checking for http-server..."
        if ! command -v http-server &> /dev/null; then
            echo "http-server not found. Installing..."
            npm install -g http-server
        fi
        echo ""
        echo "Starting http-server on http://localhost:8000"
        echo "Open http://localhost:8000/inspire-ui-analytical.html in your browser"
        echo "Press Ctrl+C to stop the server"
        echo ""
        http-server -p 8000
        ;;
    3)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid choice. Exiting..."
        exit 1
        ;;
esac

