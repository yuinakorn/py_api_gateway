# Use the official Python base image
FROM python:3.11.3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that Gunicorn will listen on
EXPOSE 8000

# Set the command to start Gunicorn
CMD ["gunicorn", "main:app", "-w", "8", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]
