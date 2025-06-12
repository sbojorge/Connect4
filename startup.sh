#!/bin/bash
# startup.sh (located in the root of your repository)

echo "--- Executing startup.sh ---"
echo "Current directory: $(pwd)"
echo "Listing contents of /app:"
ls -F /app
echo "Attempting to start Node.js application..."

# Your Node.js application (index.js) must listen on the PORT environment variable.
# Cloud Run sets this automatically.
# Ensure your index.js uses process.env.PORT for its listening port.
node index.js

# Add a message if node.js exits for some reason (though it should stay running)
echo "Node.js application exited. This should not happen."