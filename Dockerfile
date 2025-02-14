# Use Python as the base image
FROM python:3.8-slim

# Set working directory in the container
WORKDIR /app

# Copy all files from the current directory to the /app directory in the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for the Flask API
EXPOSE 5001

# Run the Flask API when the container starts
CMD ["python", "serve_model.py"]