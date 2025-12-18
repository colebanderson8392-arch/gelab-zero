# 🚀 GELab-Zero Desktop - Quick Start Guide

## 1️⃣ Prerequisites (5 minutes)

Make sure you have:
- ✅ Python 3.12+ installed
- ✅ Android device connected via USB
- ✅ USB debugging enabled on device
- ✅ Ollama running with gelab-zero-4b-preview model

## 2️⃣ Install Dependencies (1 minute)

```bash
pip install -r requirements.txt
```

## 3️⃣ Launch Desktop App (30 seconds)

Choose your platform:

### 🐧 Linux / 🍎 macOS
```bash
./run_desktop.sh
```

### 🪟 Windows
Double-click `run_desktop.bat` or run in PowerShell:
```powershell
.\run_desktop.bat
```

### 🐍 Any Platform (Python)
```bash
python desktop_launcher.py
```

## 4️⃣ Use the Application

1. **Check Device Status** 
   - Look at the sidebar to verify your device is connected
   - Click "🔄 Refresh Devices" if needed

2. **Enter a Task**
   - Type your task in natural language
   - Examples:
     - `打开微信，给柏茗发helloworld`
     - `Open WeChat and send 'hello' to TKJ`
     - `帮我在淘宝上买本书`

3. **Run the Task**
   - Click "▶️ Run Task"
   - Watch the output log for progress
   - Wait for completion

4. **View Results**
   - Click "📊 Open Visualization" to see task trajectory
   - Enter the Session ID to view detailed history

## 🎯 Optional: Install Desktop Shortcut

For easier access, install shortcuts:

```bash
python install_desktop.py
```

This creates:
- **Linux**: Application menu entry
- **macOS**: Launcher file (can add to Dock)
- **Windows**: Desktop shortcut

## 📚 Need Help?

- **Full Documentation**: See [DESKTOP_README.md](DESKTOP_README.md)
- **Technical Details**: See [DESKTOP_IMPLEMENTATION_SUMMARY.md](DESKTOP_IMPLEMENTATION_SUMMARY.md)
- **Main Project**: See [README.md](README.md)
- **Issues**: [GitHub Issues](https://github.com/stepfun-ai/gelab-zero/issues)

## ⚡ Tips

- **Port in Use?** The app runs on port 33504. Close any existing instance first.
- **No Device?** Check `adb devices` in terminal to verify connection.
- **Model Not Found?** Make sure Ollama is running: `ollama list`
- **Streamlit Not Found?** Install it: `pip install streamlit`

## 🎨 Features at a Glance

- ✨ **Modern Web UI** - Runs in your browser
- 📱 **Device Monitoring** - Real-time status
- 🚀 **One-Click Execution** - No command line needed
- 📊 **Integrated Visualization** - View task history
- 💡 **Built-in Help** - Examples and documentation
- 🌐 **Cross-Platform** - Works on Windows, macOS, Linux

---

**Enjoy using GELab-Zero Desktop! 🤖**
