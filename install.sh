#!/bin/sh

# Cleaning up before install
#docker rm -f traefik
#docker volume rm traefik

# Creating networks
#if [ -z "$(docker network list -f name=^web$ -q)" ]; then docker network create web; fi
# Creating volumes
#docker volume create traefik


# Installing and copying files to volume
#sed -i 's/^\( *\)- traefik:\/etc\/traefik:ro *$/\1- traefik:\/etc\/traefik/g' docker-compose.yml
docker-compose up --no-start
#docker cp acme.json traefik:/etc/traefik
docker cp traefik.toml traefik:/etc/traefik
docker cp toml/ traefik:/etc/traefik
#sed -i 's/^\( *\)- traefik:\/etc\/traefik *$/\1- traefik:\/etc\/traefik:ro/g' docker-compose.yml
#docker-compose up --no-start
