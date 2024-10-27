# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install compatible versions of Flask and Werkzeug directly
RUN pip install --no-cache-dir Flask==2.0.3 prometheus_flask_exporter==0.18.3 Werkzeug==2.0.3

# Copy the application code
COPY . .

# Expose port 80 for the Flask app
EXPOSE 80

# Run the Flask app
CMD ["python", "app.py"]
