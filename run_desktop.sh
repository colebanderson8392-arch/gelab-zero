#!/bin/bash
# GELab-Zero Desktop Launcher Script for Linux/macOS

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Change to script directory
cd "$SCRIPT_DIR"

# Check if Python is available
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "❌ Error: Python is not installed or not in PATH"
    exit 1
fi

# Use python3 if available, otherwise python
PYTHON_CMD=$(command -v python3 || command -v python)

# Check if streamlit is installed
if ! $PYTHON_CMD -c "import streamlit" 2>/dev/null; then
    echo "⚠️  Warning: Streamlit is not installed"
    echo "Installing dependencies..."
    $PYTHON_CMD -m pip install -r requirements.txt
fi

# Launch the desktop application
echo "🚀 Launching GELab-Zero Desktop Application..."
$PYTHON_CMD desktop_launcher.py
