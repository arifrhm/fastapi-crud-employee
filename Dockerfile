# Start with the official Python 3.10 Alpine image
FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

# Install required dependencies for building Python packages and system tools
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev cargo

# Copy requirements.txt file to install dependencies
COPY req.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r req.txt

# Copy the application code into the container
COPY . .