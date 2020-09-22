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
from depuydt import echo
from depuydt.system import Link
import hashlib

# CREATING SYMBOLIC LINKS
L = Link.create("./config", "~/docker/config/essentials")
echo.notice("Link created '" + str(L) + "' pointing to '" + str(L.target()) + "'")
