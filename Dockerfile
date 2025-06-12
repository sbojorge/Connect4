# Use node:20-slim which points to the latest slim Node.js 20 image,
# typically based on the current stable Debian release (Bookworm).
FROM node:20-slim

# Set the working directory in the container to /game.
# All subsequent RUN, CMD, ENTRYPOINT, and COPY commands will operate relative to this directory.
# Your repository's content (including its root files like package.json, index.js, startup.sh,
# and the 'game' subdirectory) will be copied into this '/game' directory.
WORKDIR /game

# --- Install Python and pip, AND build tools ---
# Update apt-get and install python3, python3-pip, AND build-essential.
# build-essential provides 'make', 'gcc', 'g++', which are needed by node-gyp for native modules.
# rm -rf /var/lib/apt/lists/* cleans up the apt cache to keep the image size down.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# --- Copy all application code ---
# Copy everything from your repository's root directory (the build context)
# into the current working directory (`/game`) inside the container.
# This single command handles copying your package.json, index.js, startup.sh,
# and the entire 'game' subdirectory.
COPY . .

# --- Install Node.js dependencies ---
# npm install --production will install dependencies based on package.json.
# Since package.json is now at /game/package.json, this will install node_modules
# into /game/node_modules.
RUN npm install --production

# --- Install Python dependencies ---
# Install Python dependencies during the build process.
# Since your 'game' subdirectory (from your repo) is now at '/game/game/'
# inside the container, the requirements.txt file will be found at './game/requirements.txt'.
# Use --break-system-packages to override the "externally-managed-environment" error on Debian/Ubuntu.
RUN python3 -m pip install --no-cache-dir -r ./game/requirements.txt --break-system-packages

# Make the startup script executable.
# startup.sh is now at /game/startup.sh.
RUN chmod +x startup.sh

# Tell Cloud Run that the application listens on the PORT environment variable
# that Cloud Run provides. Your Node.js app inside startup.sh must listen on this.
EXPOSE $PORT

# Execute your startup script when the container starts.
# startup.sh is now at /game/startup.sh.
CMD ["./startup.sh"]