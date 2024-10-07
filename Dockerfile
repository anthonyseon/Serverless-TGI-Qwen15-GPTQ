# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory contents to /app inside the container
COPY . /app

# Expose port 8000 for Flask
EXPOSE 8000

# Run the Flask app
CMD ["python", "app/modified_m2m100_flask.py"]
