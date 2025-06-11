#!/bin/bash

# --- Start Python Dependency Setup ---
echo "Starting Python dependency installation..."

# Navigate to the directory containing requirements.txt
# IMPORTANT: Adjust 'game/' if your requirements.txt is not in a 'game' subdirectory.
# For example, if requirements.txt is in the root, you'd use 'cd .' or skip this line.
cd game/

# Attempt to install Python dependencies
# 'python3 -m pip' is generally more robust than just 'pip'
# The '|| {' block will catch any errors from pip install and exit the script.
python3 -m pip install -r requirements.txt || {
  echo "ERROR: Failed to install Python dependencies during startup. Check pip output above."
  exit 1
}

echo "Python dependencies installed successfully."

# Add the temporary installation directory to PYTHONPATH if needed
# App Engine's default pip install usually puts packages in a standard location
# that Python can find automatically. You might not need this line.
# If your Python scripts need to import from a specific 'lib' folder,
# you'll need to adjust where pip installs packages (e.g., pip install -t lib).
# For now, let's keep it simple and assume default install location works.
# export PYTHONPATH=/tmp/python_deps:$PYTHONPATH # Re-add if your Python code can't find installed packages


# Navigate back to the root of your application (if you changed directory)
# This assumes your index.js is in the root or an expected location relative to the root.
cd -

# --- End Python Dependency Setup ---


echo "Starting Node.js application..."

# Start your Node.js application
# This should be the last command in the script
# App Engine will automatically set the PORT environment variable.
# Your Node.js app (index.js) must listen on this port.
node index.js