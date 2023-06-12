#!/bin/bash
## --------------------------------------------------------------------------------
## Purpose: Running the docker image from docker-hub
## --------------------------------------------------------------------------------

set -e

# Check if Docker service is running and start if not
if ! systemctl is-active --quiet docker; then
    echo "Starting Docker service..."
    systemctl start docker
fi

# Check if the Docker container is running, if yes remove it
if docker inspect -f '{{.State.Running}}' bpo_app >/dev/null 2>&1; then
    echo "Stopping and removing existing bpo_app container..."
    docker stop bpo_app >/dev/null
    docker rm bpo_app >/dev/null
fi

# Pull the Docker image
echo "Pulling the latest bpo image from Docker Hub..."
docker pull asafbm/bpo:latest

# Run the container on localhost
echo "Starting the bpo_app container..."
docker run --name bpo_app -d -p 8080:8050 asafbm/bpo:latest

echo "bpo application will be opened at http://127.0.0.1:8080/"

# Open the browser and wait for it to load
echo "Opening the browser..."
# it will work only if you have xdg install on your machine, else use something else or just open the browser :)
xdg-open http://127.0.0.1:8080/
sleep 2

# Send the F5 key to refresh the page
echo "Refreshing the page... refresh the browser page if necessary"
xdotool key XF86WakeUp && xdotool key F5
