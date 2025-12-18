#!/usr/bin/env python3
"""
GELab-Zero Desktop Application
A Streamlit-based desktop interface for running GELab-Zero tasks
"""

import streamlit as st
import subprocess
import sys
import os
import time
from pathlib import Path
import threading
import queue

if "." not in sys.path:
    sys.path.append(".")

# Page configuration
st.set_page_config(
    page_title="GELab-Zero Desktop",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better appearance
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .status-box {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .success {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
    }
    .error {
        background-color: #f8d7da;
        border-left: 4px solid #dc3545;
    }
    .info {
        background-color: #d1ecf1;
        border-left: 4px solid #17a2b8;
    }
    .warning {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'task_running' not in st.session_state:
    st.session_state.task_running = False
if 'task_output' not in st.session_state:
    st.session_state.task_output = []
if 'device_status' not in st.session_state:
    st.session_state.device_status = None

def check_devices():
    """Check for connected Android devices"""
    try:
        from copilot_front_end.mobile_action_helper import list_devices
        devices = list_devices()
        return devices
    except Exception as e:
        return None

def run_task_subprocess(task, output_queue):
    """Run task in subprocess and send output to queue"""
    try:
        cmd = [sys.executable, "examples/run_single_task.py", task]
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        for line in process.stdout:
            output_queue.put(('output', line))
        
        process.wait()
        output_queue.put(('done', process.returncode))
    except Exception as e:
        output_queue.put(('error', str(e)))

# Header
st.markdown('<div class="main-header">🤖 GELab-Zero Desktop</div>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Device status
    st.subheader("📱 Device Status")
    if st.button("🔄 Refresh Devices", use_container_width=True):
        with st.spinner("Checking devices..."):
            st.session_state.device_status = check_devices()
    
    # Check devices on first load
    if st.session_state.device_status is None:
        st.session_state.device_status = check_devices()
    
    if st.session_state.device_status:
        st.success(f"✓ {len(st.session_state.device_status)} device(s) connected")
        for idx, device in enumerate(st.session_state.device_status):
            st.text(f"  {idx+1}. {device}")
    else:
        st.warning("⚠️ No devices found")
        st.info("Please connect an Android device via USB with ADB debugging enabled.")
    
    st.markdown("---")
    
    # Quick actions
    st.subheader("🚀 Quick Actions")
    
    if st.button("📊 Open Visualization", use_container_width=True):
        st.info("Opening visualization in new tab...")
        st.markdown("[Click here to open visualization](http://localhost:33503)", unsafe_allow_html=True)
    
    if st.button("📁 View Logs", use_container_width=True):
        log_path = "running_log/server_log/os-copilot-local-eval-logs"
        if os.path.exists(log_path):
            st.success(f"Log directory: `{log_path}`")
        else:
            st.warning("No logs found yet. Run a task first.")
    
    st.markdown("---")
    
    # Help & Info
    st.subheader("ℹ️ Information")
    with st.expander("📖 How to Use"):
        st.markdown("""
        1. **Connect Device**: Connect your Android device via USB
        2. **Enable ADB**: Make sure USB debugging is enabled
        3. **Enter Task**: Type your task in natural language
        4. **Run**: Click 'Run Task' to execute
        5. **Monitor**: Watch the output log in real-time
        """)
    
    with st.expander("💡 Example Tasks"):
        st.markdown("""
        - `打开微信，给柏茗发helloworld`
        - `Open WeChat and send 'hello' to TKJ`
        - `帮我在淘宝上买本书`
        - `Go to Hema Fresh Store and add items to cart`
        """)
    
    with st.expander("🔗 Links"):
        st.markdown("""
        - [GitHub Repository](https://github.com/stepfun-ai/gelab-zero)
        - [Documentation](./DESKTOP_README.md)
        - [Technical Report](https://arxiv.org/abs/2512.15431)
        """)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📝 Task Input")
    
    task = st.text_area(
        "Enter your task:",
        value="打开微信，给柏茗发helloworld",
        height=100,
        help="Describe what you want the agent to do in natural language"
    )
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
    
    with col_btn1:
        run_button = st.button(
            "▶️ Run Task",
            disabled=st.session_state.task_running or not st.session_state.device_status,
            use_container_width=True,
            type="primary"
        )
    
    with col_btn2:
        clear_button = st.button("🗑️ Clear Log", use_container_width=True)
    
    if clear_button:
        st.session_state.task_output = []
        st.rerun()

with col2:
    st.header("📊 Status")
    
    if st.session_state.task_running:
        st.markdown('<div class="status-box info">⏳ Task is running...</div>', unsafe_allow_html=True)
    elif st.session_state.device_status:
        st.markdown('<div class="status-box success">✓ Ready to run tasks</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-box warning">⚠️ No device connected</div>', unsafe_allow_html=True)

# Task execution
if run_button:
    if not task.strip():
        st.error("❌ Please enter a task!")
    else:
        st.session_state.task_running = True
        st.session_state.task_output = []
        st.session_state.task_output.append(f"🚀 Starting task: {task}")
        st.session_state.task_output.append("=" * 60)
        
        # Run task
        output_queue = queue.Queue()
        thread = threading.Thread(target=run_task_subprocess, args=(task, output_queue))
        thread.daemon = True
        thread.start()
        
        # Create placeholder for output
        output_placeholder = st.empty()
        
        # Monitor task output
        with st.spinner("Running task..."):
            while thread.is_alive() or not output_queue.empty():
                try:
                    msg_type, msg_content = output_queue.get(timeout=0.1)
                    
                    if msg_type == 'output':
                        st.session_state.task_output.append(msg_content.rstrip())
                    elif msg_type == 'done':
                        if msg_content == 0:
                            st.session_state.task_output.append("=" * 60)
                            st.session_state.task_output.append("✅ Task completed successfully!")
                        else:
                            st.session_state.task_output.append("=" * 60)
                            st.session_state.task_output.append(f"❌ Task failed with exit code {msg_content}")
                        st.session_state.task_running = False
                        break
                    elif msg_type == 'error':
                        st.session_state.task_output.append("=" * 60)
                        st.session_state.task_output.append(f"❌ Error: {msg_content}")
                        st.session_state.task_running = False
                        break
                    
                    # Update output display
                    output_placeholder.code('\n'.join(st.session_state.task_output), language='text')
                    
                except queue.Empty:
                    time.sleep(0.1)
        
        st.rerun()

# Output log
st.header("📋 Output Log")

if st.session_state.task_output:
    output_text = '\n'.join(st.session_state.task_output)
    st.code(output_text, language='text', line_numbers=False)
else:
    st.info("👆 Enter a task above and click 'Run Task' to see output here")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>GELab-Zero Desktop v1.0 | "
    "© 2025 GELab Team</div>",
    unsafe_allow_html=True
)
