@echo off
REM GELab-Zero Desktop Launcher Script for Windows

echo ============================================================
echo GELab-Zero Desktop Application
echo ============================================================
echo.

REM Get the directory where this script is located
cd /d "%~dp0"

REM Check if Python is available
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.12+ from https://www.python.org/
    pause
    exit /b 1
)

REM Check if streamlit is installed
python -c "import streamlit" >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Warning: Streamlit is not installed
    echo Installing dependencies...
    python -m pip install -r requirements.txt
)

REM Launch the desktop application
echo.
echo Starting GELab-Zero Desktop Application...
echo.
python desktop_launcher.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Application exited with an error
    pause
)
