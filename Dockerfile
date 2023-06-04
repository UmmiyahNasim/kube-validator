# Use the Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script and requirements files to the working directory
COPY main.py .
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint command
ENTRYPOINT ["python", "main.py"]

