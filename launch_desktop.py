#!/usr/bin/env python3
import sys
import os

# Add project directory to path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Launch desktop app
from desktop_launcher import main
main()
