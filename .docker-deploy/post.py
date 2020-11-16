#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

## INCLUDES
from depuydt import docker

# Installing and copying files to volume
docker.Compose.exec("traefik","","rm -r /etc/traefik/toml")
docker.cp("config/traefik/traefik.toml","traefik:/etc/traefik")
docker.cp("config/traefik/toml","traefik:/etc/traefik")