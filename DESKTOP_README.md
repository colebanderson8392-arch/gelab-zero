# GELab-Zero Desktop Application

This desktop application provides a user-friendly graphical interface for running GELab-Zero tasks on your desktop computer.

## Features

- **Simple GUI Interface**: Easy-to-use graphical interface for task input and execution
- **Real-time Output**: View task execution logs in real-time
- **Visualization Integration**: Quick access to Streamlit visualization dashboard
- **Device Management**: Check connected Android devices
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Quick Start

### Prerequisites

Make sure you have completed the basic setup from the main [README.md](README.md):

1. Python 3.12+ environment installed
2. LLM inference environment (Ollama or vLLM) set up
3. Android device connected via ADB
4. All dependencies installed: `pip install -r requirements.txt`

### Installation

#### Option 1: Automatic Installation (Recommended)

Run the installation script to create desktop shortcuts:

```bash
python install_desktop.py
```

This will create platform-specific shortcuts:
- **Linux**: Desktop entry in your application menu
- **macOS**: Launcher command file that can be added to Dock
- **Windows**: Batch file and desktop shortcut

#### Option 2: Manual Launch

You can directly launch the desktop application without installation:

```bash
python desktop_launcher.py
```

Or use the simple launcher:

```bash
python launch_desktop.py
```

## Usage

### Main Interface

The desktop application provides a clean interface with the following sections:

1. **Task Input**: Enter your task description in natural language
2. **Control Buttons**:
   - **Run Task**: Execute the entered task
   - **Open Visualization**: Launch the Streamlit visualization dashboard
   - **Stop**: Stop a running task
3. **Output Log**: Real-time display of task execution logs
4. **Status Bar**: Shows current application status and device connection

### Running a Task

1. Make sure your Android device is connected via USB and ADB debugging is enabled
2. Enter your task in the task input field, for example:
   - "打开微信，给柏茗发helloworld" (Chinese)
   - "Open WeChat and send 'hello world' to TKJ" (English)
   - "帮我在淘宝上买本书" (Search for books on Taobao)
3. Click "Run Task" to start execution
4. Monitor the progress in the output log
5. Wait for the task to complete

### Viewing Task History

1. Click "Open Visualization" to launch the Streamlit dashboard
2. Enter the Session ID from a completed task
3. View the detailed trajectory with screenshots and actions

### Menu Options

**File Menu:**
- Check Devices: Verify Android device connection
- Exit: Close the application

**Tools Menu:**
- Open Visualization: Launch Streamlit visualization server
- Open Log Directory: Open the folder containing task logs

**Help Menu:**
- Documentation: Open GitHub documentation
- About: Show application information

## Configuration

The desktop launcher uses the same configuration as the command-line version:

- Model configuration: `model_config.yaml`
- MCP server configuration: `mcp_server_config.yaml`
- Task execution settings: `examples/run_single_task.py`

## Troubleshooting

### "No devices found" Error

1. Check USB connection to your Android device
2. Verify USB debugging is enabled on your device
3. Run `adb devices` in terminal to confirm device is recognized
4. Click "File" → "Check Devices" in the application

### Task Execution Fails

1. Ensure Ollama is running with the gelab-zero-4b-preview model
2. Check that all dependencies are installed: `pip install -r requirements.txt`
3. Verify your device has necessary permissions enabled
4. Check the output log for specific error messages

### Visualization Won't Open

1. Make sure Streamlit is installed: `pip install streamlit`
2. Check if port 33503 is available (not in use by another application)
3. Try manually starting visualization: `streamlit run visualization/main_page.py --server.port 33503`

## Advanced Usage

### Custom Task Configuration

To modify task execution parameters, edit `examples/run_single_task.py`:

```python
local_model_config = {
    "task_type": "parser_0922_summary",
    "model_config": {
        "model_name": "gelab-zero-4b-preview",
        "model_provider": "local",
        "args": {
            "temperature": 0.1,
            "top_p": 0.95,
            "max_tokens": 4096,
        },
    },
    "max_steps": 400,
    "delay_after_capture": 2,
}
```

### Multiple Devices

If you have multiple Android devices connected, the application will use the first device found. To use a specific device, you can modify the device selection logic in the desktop launcher.

## System Requirements

- **Operating System**: Windows 10+, macOS 10.14+, or Linux (with X11/Wayland)
- **Python**: 3.12 or higher
- **RAM**: 8GB minimum (16GB recommended for model inference)
- **GPU**: Optional but recommended for faster inference
- **Android Device**: Android 7.0+ with USB debugging enabled

## Architecture

The desktop application is built with:
- **GUI Framework**: Streamlit (web-based UI framework)
- **Task Execution**: Subprocess management of the existing CLI tools
- **Visualization**: Integrated Streamlit interface for both task running and trajectory viewing
- **Device Communication**: Existing ADB integration from copilot_front_end

The application runs as a local web server and opens in your default browser, providing a modern and responsive interface without requiring additional GUI dependencies.

## Contributing

To contribute to the desktop application:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test on multiple platforms if possible
5. Submit a pull request

## License

Same as the main GELab-Zero project.

## Support

For issues specific to the desktop application, please:
1. Check this README and troubleshooting section
2. Refer to the main [README.md](README.md) for general setup
3. Open an issue on GitHub with the "desktop" label

## Future Enhancements

Planned features for future versions:
- [ ] Task templates and favorites
- [ ] Multi-device support with selection
- [ ] Enhanced visualization integration
- [ ] Task history browser
- [ ] Settings panel for configuration
- [ ] Dark mode support
- [ ] Task scheduling and automation
