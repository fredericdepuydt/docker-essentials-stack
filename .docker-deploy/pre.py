#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

## INCLUDES
#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

## INCLUDES
from depuydt import command, environment
import hashlib


# CREATING SYMBOLIC LINKS
command.exec("mkdir ./config")
command.exec("ln -s ~/docker/config/traefik ./config/traefik")
command.exec("ln -s ~/docker/config/portainer ./config/portainer")
command.exec("ln -s ~/docker/config/authelia ./config/authelia")
