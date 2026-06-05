# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install system dependencies and Node.js
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt

# Copy and install Node.js dependencies
COPY frontend/package*.json ./frontend/
RUN cd frontend && npm install

# Copy the rest of the application code into the container
COPY . .

# Build the frontend CSS
RUN cd frontend && npm run build:css

# Make the start script executable
RUN chmod +x start.sh

# Expose ports for both backend (8000) and frontend (3000)
EXPOSE 8000
EXPOSE 3000

# Run the shell script to start both services
CMD ["./start.sh"]
