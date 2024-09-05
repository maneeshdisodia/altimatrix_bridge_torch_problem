# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install pytest

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run pytest when the container launches
CMD ["pytest", "bridge_crossing.py"]