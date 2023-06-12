#!/bin/bash

## --------------------------------------------------------------------------------
## Purpose: This script builds a Docker image for the Dash app.
## This script stops and removes all running containers, removes unused volumes, networks, and build cache,
## deletes dangling images and all images, and cleans up all Docker resources.
##
## !! WARNING !!
## Use with caution. This script will delete the current app container if it exists and remove logs from the app.
## Ensure important data or images are backed up.
## This script has no turn back.
## --------------------------------------------------------------------------------


# Move to the root directory of the project
cd ../..

# Define the file and line range to comment out
FILE="app/main.py"
START_LINE=52

# Comment out the lines from START_LINE to the end of the file if they are not already commented out
sed -i "${START_LINE},\$ { /^[[:blank:]]*#/! s/^/#/ }" "$FILE"
echo "Lines $START_LINE to the end of $FILE have been commented out if not already."


# Remove old logs from the app
> app/logs/app_logs/all_logs.log
> app/logs/app_logs/system_logs.log


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
