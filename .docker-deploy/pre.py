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
<<<<<<< HEAD
from depuydt import echo
from depuydt.system import Link
import hashlib

# CREATING SYMBOLIC LINKS
L = Link.create("./config", "~/docker/config/essentials")
echo.notice("Link created '" + str(L) + "' pointing to '" + str(L.target()) + "'")
=======
from depuydt import command, environment
import hashlib


# CREATING SYMBOLIC LINKS
command.exec("mkdir ./config")
command.exec("ln -s ~/docker/config/traefik ./config/traefik")
command.exec("ln -s ~/docker/config/portainer ./config/portainer")
command.exec("ln -s ~/docker/config/authelia ./config/authelia")
>>>>>>> 0971605d06bdb94c933ea752d46da5907eaaeb0b
