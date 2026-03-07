#!/bin/bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add current user to docker group to run without sudo
sudo usermod -aG docker $USER

# Install Docker Compose plugin (if not installed by script)
sudo apt-get update
sudo apt-get install -y docker-compose-plugin

echo "Docker installed successfully! Please log out and log back in (or restart your shell) for group changes to take effect."
