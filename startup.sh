#!/bin/bash

echo "Starting App Engine startup script..."

# Ensure pip is for python3 and install dependencies
# The -t /tmp/python_deps flag installs packages to a temporary directory.
# We then add this directory to PYTHONPATH so Python can find them.
# This avoids modifying system-wide packages or needing write access to common locations.
echo "Installing Python dependencies from python_game/requirements.txt..."
python3 -m pip install -r python_game/requirements.txt --target=/tmp/python_deps

# Check if pip installation was successful
if [ $? -ne 0 ]; then
  echo "ERROR: Failed to install Python dependencies. Please check requirements.txt and logs."
  exit 1
fi

# Add the temporary installation directory to PYTHONPATH
# This makes the installed packages available to your run.py script
export PYTHONPATH=/tmp/python_deps:$PYTHONPATH

echo "Python dependencies installed successfully. Starting Node.js application..."

# Start your Node.js application
# This should be the last command in the script
node index.js