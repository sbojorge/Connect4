# Use a Node.js base image that's based on Debian (e.g., Bookworm),
# as this makes it easy to install Python via apt.
FROM node:20-slim

# Set the working directory in the container
WORKDIR /app

# --- Install Python and pip ---
# Update apt-get and install python3 and python3-pip
# --no-install-recommends helps keep the image size down
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    curl && \
    rm -rf /var/lib/apt/lists/*

# --- Install Node.js dependencies ---
# Copy package.json and package-lock.json first to leverage Docker cache
COPY package.json ./
# If you use yarn, use `COPY yarn.lock .` and `RUN yarn install --production`
RUN npm install --production

# --- Install Python dependencies ---
# Copy your game/ directory which contains requirements.txt
COPY game/ game/
# Install Python dependencies during the build process
# This is more robust than trying to install them in startup.sh at runtime.
RUN python3 -m pip install --no-cache-dir -r game/requirements.txt

# --- Copy the rest of your application code ---
# This includes your index.js and startup.sh
COPY . .

# Make the startup script executable
RUN chmod +x startup.sh

# Tell Cloud Run that the application listens on the PORT environment variable
# that Cloud Run provides. Your Node.js app inside startup.sh must listen on this.
EXPOSE $PORT

# Execute your startup script when the container starts
CMD ["./startup.sh"]