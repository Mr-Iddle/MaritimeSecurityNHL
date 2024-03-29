#!/bin/bash
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ee:latest
echo "Open a webbrowser and got to https://localhost:9443"

# FOR LINUX This script is responsible for easier start of the portainer (docker management tool) for the team mates.

# portainerRunning.bat is made specifically for Windows users. 