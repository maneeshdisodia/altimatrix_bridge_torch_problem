#!/bin/bash

# Build the Docker image
docker build -t bridge-crossing .

# Run the tests inside the container
docker run bridge-crossing
