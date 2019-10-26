#!/bin/sh
############################################################################
## Raspberry-Pi installation script                                       ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
##                                                                        ##
## Executing this script requires the 'depuydt' shell libraries           ##
############################################################################

## INCLUDES
. /usr/local/lib/depuydt/sh/echoes.sh

## TITLE
echo_section "DOCKER DEPLOYING:" "Essentials Stack (Installing)"

# Creating external networks
if [ -z "$(docker network list -f name=^web$ -q)" ]; then docker network create web; fi

# Installing and copying files to volume
#sed -i 's/^\( *\)- traefik:\/etc\/traefik:ro *$/\1- traefik:\/etc\/traefik/g' docker-compose.yml
docker-compose up --no-start
#docker cp acme.json traefik:/etc/traefik
docker cp traefik.toml traefik:/etc/traefik
docker cp toml/ traefik:/etc/traefik
#sed -i 's/^\( *\)- traefik:\/etc\/traefik *$/\1- traefik:\/etc\/traefik:ro/g' docker-compose.yml
#docker-compose up --no-start
