#!/bin/bash

# Start the FastAPI backend in the background
echo "Starting Python FastAPI Backend on port 8000..."
python app.py &
BACKEND_PID=$!

# Wait a few seconds for the backend to initialize
sleep 5

# Start the Node.js frontend in the foreground
echo "Building Frontend CSS..."
cd frontend && npm run build:css
echo "Starting Node.js Frontend on port 3000..."
node server.js &
FRONTEND_PID=$!

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
