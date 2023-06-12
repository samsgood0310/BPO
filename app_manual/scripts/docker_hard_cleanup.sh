#!/bin/bash

## --------------------------------------------------------------------------------
## Purpose: Hard cleanup of all docker components on this machine
## This script stops and removes all running containers,
## removes unused volumes, networks, and build cache
## deletes dangling images and all images,
## and cleans up all Docker resources.
##
## !! WARNING!!
## Use with caution. Ensure important data or images are backed up.
## This script have no turn back
## --------------------------------------------------------------------------------


# About section
echo "Docker Cleanup Script"

# Stop and remove all running containers
echo "Stopping and removing all running containers..."
docker stop $(docker ps -aq)
docker rm -f $(docker ps -aq)
echo "All running containers have been stopped and removed."

# Remove unused volumes
echo "Removing unused volumes..."
docker volume prune -f
echo "Unused volumes have been removed."

# Remove unused networks
echo "Removing unused networks..."
docker network prune -f
echo "Unused networks have been removed."

# Remove unused build cache
echo "Removing unused build cache..."
docker builder prune -af
echo "Unused build cache has been removed."

# Remove dangling images
echo "Removing dangling images..."
docker image prune -af
echo "Dangling images have been removed."

# Remove all images
echo "Removing all images..."
docker rmi -f $(docker images -aq)
echo "All images have been removed."

# Clean up all Docker resources
echo "Cleaning up all Docker resources..."
docker system prune -af
echo "All Docker resources have been cleaned up."

# Done
echo "Cleanup process complete."
