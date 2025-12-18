#!/usr/bin/env python3
"""
GELab-Zero Desktop Application Launcher
Launches the Streamlit-based desktop interface
"""

import subprocess
import sys
import os
import webbrowser
import time
from pathlib import Path

# Add parent directory to path
if "." not in sys.path:
    sys.path.append(".")

def check_streamlit():
    """Check if streamlit is available"""
    try:
        import streamlit
        return True
    except ImportError:
        return False

def launch_desktop_app():
    """Launch the Streamlit-based desktop application"""
    print("=" * 60)
    print("GELab-Zero Desktop Application")
    print("=" * 60)
    print()
    
    if not check_streamlit():
        print("❌ Error: Streamlit is not installed.")
        print("Please install it with: pip install streamlit")
        return False
    
    print("🚀 Starting GELab-Zero Desktop Application...")
    print()
    print("📋 The application will open in your default web browser.")
    print("🌐 URL: http://localhost:33504")
    print()
    print("⚠️  To stop the application, press Ctrl+C in this terminal")
    print("=" * 60)
    print()
    
    # Change to project directory
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # Launch streamlit app
    cmd = [
        sys.executable, "-m", "streamlit", "run",
        "desktop_app.py",
        "--server.port", "33504",
        "--server.address", "localhost",
        "--browser.gatherUsageStats", "false"
    ]
    
    try:
        # Run streamlit (this blocks until stopped)
        # Streamlit will automatically open the browser
        subprocess.run(cmd, check=True)
        
    except KeyboardInterrupt:
        print("\n\n✓ Application stopped by user")
        return True
    except Exception as e:
        print(f"\n❌ Error launching application: {e}")
        return False
    
    return True

def main():
    """Main entry point"""
    success = launch_desktop_app()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
