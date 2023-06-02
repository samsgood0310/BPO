#!/bin/bash

## --------------------------------------------------------------------------------
## Purpose: Upload / update the docker-image in dockerhub
## This script will build, tag and push your docker-image to dockerhub

## !! WARNING!!
## Make sure to remove your DOCKERHUB_PASSWORD before committing or saving this file
## --------------------------------------------------------------------------------


# Set the parameters
IMAGE_NAME="bpo-image"
DOCKERHUB_USERNAME="<YOUR-DOCKERHUB-USERNAME>"
TAG_NAME="latest"
REPOSITORY_NAME="bpo"
DOCKERHUB_PASSWORD="<YOUR-DOCKERHUB-PASSWORD>"


# Step 0: turn on docker if needed
if ! systemctl is-active --quiet docker; then
    echo "Starting Docker service..."
    systemctl start docker
fi

# Step 1: Move to the root directory of the project
cd ../..

# Step 2: Build the Docker image
echo "Building the Docker image..."
docker build -t $IMAGE_NAME .
echo "Docker image '$IMAGE_NAME' built."

# Step 3: Tag the Docker image
echo "Tagging the Docker image..."
docker tag $IMAGE_NAME $DOCKERHUB_USERNAME/$REPOSITORY_NAME:$TAG_NAME
echo "Docker image tagged."

# Step 4: Log in to Docker Hub
echo "Logging in to Docker Hub..."
echo $DOCKERHUB_PASSWORD | docker login --username $DOCKERHUB_USERNAME --password-stdin
echo "Logged in to Docker Hub."

# Step 5: Push the Docker image
echo "Pushing the Docker image to Docker Hub..."
docker push $DOCKERHUB_USERNAME/$REPOSITORY_NAME:$TAG_NAME
echo "Docker image pushed to Docker Hub."
