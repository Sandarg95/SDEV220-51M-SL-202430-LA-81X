# Use Python 3.11 based on Debian Bookworm
FROM python:3.11-bookworm

# Set the working directory in the container
WORKDIR /app

# Install any required dependencies (e.g., system libraries, packages)
RUN apt-get update && apt-get install -y \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the Flask application code into the container
COPY . /app

# Install the Python dependencies (Flask, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
