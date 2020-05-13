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
sys.path.insert(1, '/home/pi/installation/lib/depuydt/python/');
#sys.path.insert(1, '/usr/local/lib/depuydt/python/')

from echo import echo
from docker import docker
from environment import environment
from mysql import mysql

## TITLE
echo.section("DOCKER DEPLOYING", "Essentials Stack (Installing)");

## Checking external networks
docker.network.exists("web");

## Creating the volumes, networks and containers
docker.compose.up("--build --no-start");

# Installing and copying files to volume
#sed -i 's/^\( *\)- traefik:\/etc\/traefik:ro *$/\1- traefik:\/etc\/traefik/g' docker-compose.yml
#docker-compose up --no-start
#docker cp acme.json traefik:/etc/traefik
#docker cp traefik.toml essentials-traefik:/etc/traefik
#docker cp toml/ essentials-traefik:/etc/traefik
#sed -i 's/^\( *\)- traefik:\/etc\/traefik *$/\1- traefik:\/etc\/traefik:ro/g' docker-compose.yml
