#!/bin/bash
# startup.sh (located in the root of your repository)

echo "Starting Node.js application..."

# Your Node.js application (index.js) must listen on the PORT environment variable.
# Cloud Run sets this automatically.
# Ensure your index.js uses process.env.PORT for its listening port.
node index.js