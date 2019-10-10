sed -i 's/^\( *\)- traefik-conf:\/etc\/traefik:ro *$/\1- traefik-conf:\/etc\/traefik/g' docker-compose.yml
docker-compose up --no-start
docker cp traefik.toml traefik:/etc/traefik
docker cp toml/ traefik:/etc/traefik
sed -i 's/^\( *\)- traefik-conf:\/etc\/traefik *$/\1- traefik-conf:\/etc\/traefik:ro/g' docker-compose.yml
docker-compose up -d
