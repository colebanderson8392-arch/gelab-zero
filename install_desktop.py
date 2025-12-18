#!/usr/bin/env python3
"""
Desktop Installation Script for GELab-Zero
This script installs desktop shortcuts for Windows, macOS, and Linux
"""

import os
import sys
import platform
import subprocess
from pathlib import Path

def get_project_root():
    """Get the absolute path to the project root"""
    return Path(__file__).parent.absolute()

def install_linux():
    """Install desktop entry for Linux"""
    print("Installing GELab-Zero for Linux...")
    
    project_root = get_project_root()
    desktop_file_content = f"""[Desktop Entry]
Version=1.0
Type=Application
Name=GELab-Zero
Comment=GUI Agent Platform for Mobile Automation
Exec={sys.executable} {project_root}/desktop_launcher.py
Icon={project_root}/images/main_en.png
Terminal=false
Categories=Development;Utility;
Keywords=AI;Agent;Automation;
"""
    
    # Create .desktop file
    desktop_dir = Path.home() / ".local" / "share" / "applications"
    desktop_dir.mkdir(parents=True, exist_ok=True)
    
    desktop_file = desktop_dir / "gelab-zero.desktop"
    with open(desktop_file, "w") as f:
        f.write(desktop_file_content)
    
    # Make it executable
    os.chmod(desktop_file, 0o755)
    
    print(f"✓ Desktop entry created at: {desktop_file}")
    print("✓ GELab-Zero should now appear in your application menu")
    
    # Try to update desktop database
    try:
        subprocess.run(["update-desktop-database", str(desktop_dir)], 
                      capture_output=True, check=False)
    except:
        pass
    
    return True

def install_macos():
    """Install application bundle for macOS"""
    print("Installing GELab-Zero for macOS...")
    
    project_root = get_project_root()
    
    # Create a launcher script
    launcher_script = project_root / "run_gelab_desktop.command"
    script_content = f"""#!/bin/bash
cd "{project_root}"
{sys.executable} desktop_launcher.py
"""
    
    with open(launcher_script, "w") as f:
        f.write(script_content)
    
    os.chmod(launcher_script, 0o755)
    
    print(f"✓ Launcher script created at: {launcher_script}")
    print("✓ You can double-click 'run_gelab_desktop.command' to launch GELab-Zero")
    print("✓ Or drag it to your Dock for quick access")
    
    return True

def install_windows():
    """Install shortcut for Windows"""
    print("Installing GELab-Zero for Windows...")
    
    project_root = get_project_root()
    
    # Create a batch file launcher
    batch_file = project_root / "GELab-Zero.bat"
    batch_content = f"""@echo off
cd /d "{project_root}"
"{sys.executable}" desktop_launcher.py
pause
"""
    
    with open(batch_file, "w") as f:
        f.write(batch_content)
    
    print(f"✓ Launcher batch file created at: {batch_file}")
    
    # Try to create a shortcut on desktop using PowerShell
    try:
        desktop = Path.home() / "Desktop"
        shortcut_path = desktop / "GELab-Zero.lnk"
        
        ps_script = f"""
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
$Shortcut.TargetPath = "{batch_file}"
$Shortcut.WorkingDirectory = "{project_root}"
$Shortcut.Description = "GELab-Zero Desktop Application"
$Shortcut.Save()
"""
        
        result = subprocess.run(
            ["powershell", "-Command", ps_script],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            print(f"✓ Desktop shortcut created at: {shortcut_path}")
        else:
            print(f"⚠ Could not create desktop shortcut automatically.")
            print(f"  You can manually create a shortcut to: {batch_file}")
    
    except Exception as e:
        print(f"⚠ Could not create desktop shortcut: {e}")
        print(f"  You can manually create a shortcut to: {batch_file}")
    
    return True

def create_simple_launcher():
    """Create a simple Python launcher script as fallback"""
    project_root = get_project_root()
    launcher = project_root / "launch_desktop.py"
    
    content = """#!/usr/bin/env python3
import sys
import os

# Add project directory to path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Launch desktop app
from desktop_launcher import main
main()
"""
    
    with open(launcher, "w") as f:
        f.write(content)
    
    os.chmod(launcher, 0o755)
    print(f"✓ Simple launcher created at: {launcher}")

def main():
    """Main installation function"""
    print("=" * 60)
    print("GELab-Zero Desktop Installation")
    print("=" * 60)
    print()
    
    system = platform.system()
    
    try:
        if system == "Linux":
            success = install_linux()
        elif system == "Darwin":
            success = install_macos()
        elif system == "Windows":
            success = install_windows()
        else:
            print(f"⚠ Unsupported operating system: {system}")
            success = False
        
        # Always create simple launcher as fallback
        create_simple_launcher()
        
        print()
        print("=" * 60)
        if success:
            print("✓ Installation completed successfully!")
            print()
            print("To launch GELab-Zero Desktop:")
            print(f"  python {get_project_root()}/desktop_launcher.py")
            print()
            print("Or use the launcher created for your system.")
        else:
            print("⚠ Installation completed with warnings.")
            print()
            print("You can still launch GELab-Zero using:")
            print(f"  python {get_project_root()}/desktop_launcher.py")
        print("=" * 60)
        
    except Exception as e:
        print(f"✗ Installation failed: {e}")
        print()
        print("You can still launch GELab-Zero using:")
        print(f"  python {get_project_root()}/desktop_launcher.py")
        return False
    
    return True

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
