#!/usr/bin/env python3

############################################################################
## Raspberry-Pi installation script                                       ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
##                                                                        ##
## Executing this script requires the 'depuydt' python libraries          ##
############################################################################

## INCLUDES
import sys
sys.path.insert(1, '/usr/local/lib/depuydt/python/')

from echo import echo
from docker import docker
from environment import environment
from mysql import mysql

## TITLE
echo.section("DOCKER DEPLOYING", "Essentials Stack (Installing)");

## Checking external networks
docker.network.exists("web");

portainer_password = environment.get("PORTAINER_PASSWORD",True);
portainer_password = environment.get("PORTAINER_PASSWORD_HASH",True);

## Creating the volumes, networks and containers
docker.compose.up("--build --no-start");

# Installing and copying files to volume
#sed -i 's/^\( *\)- traefik:\/etc\/traefik:ro *$/\1- traefik:\/etc\/traefik/g' docker-compose.yml
docker.cp("traefik/traefik.toml","traefik:/etc/traefik");
docker.cp("traefik/toml/","traefik:/etc/traefik");
#docker.cp("traefik/acme.json","traefik:/etc/acme");
#sed -i 's/^\( *\)- traefik:\/etc\/traefik *$/\1- traefik:\/etc\/traefik:ro/g' docker-compose.yml
