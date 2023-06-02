#!/bin/bash

# This script build a docker-image for the dash-app.


# Move to the root directory of the project
cd ../..

# Define the file and line range to comment out
FILE="app/main.py"
START_LINE=51

# Comment out the lines from START_LINE to the end of the file if they are not already commented out
sed -i "${START_LINE},\$ { /^[[:blank:]]*#/! s/^/#/ }" "$FILE"
echo "Lines $START_LINE to the end of $FILE have been commented out if not already."

# Check if Docker service is running, if not start Docker
if ! systemctl is-active --quiet docker; then
    systemctl start docker
    echo "Docker service started."
fi

# Check if the Docker container is running, if yes remove it
if docker inspect -f '{{.State.Running}}' bpo_app >/dev/null 2>&1; then
    docker rm -f bpo_app
    echo "Existing Docker container 'bpo_app' removed."
fi

# Build the Docker image
docker build -t bin-packing .
echo "Docker image 'bin-packing' built."

# Run the Docker container
docker run --name bpo_app -p 8050:8050 bin-packing
echo "Docker container 'bpo_app' is now running."
