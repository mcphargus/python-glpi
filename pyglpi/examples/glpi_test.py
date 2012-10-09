#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os

# nothing is packaged yet, and I'm trying to not depend on my custom
# environment vars for everthing, so.....
glpimodpath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.split(glpimodpath)[0])

# now this part should work:
from GLPI import GLPIClient

if __name__ == '__main__':

    import warnings
    import getpass
    import pprint    

    try:
        host = os.environ['GLPI_SERVERNAME']
    except:
        warnings.warn("GLPI environment variables not locally set", RuntimeWarning)
        host = raw_input("Enter your GLPI hostname: ")
    
    glpi = GLPIClient()
    # my servers are configured with the glpi root under VirtualHost
    # configurations, BASEURL changed accordingly on next line.
    glpi.BASEURL = ''
    glpi.connect(host)

    pprint.pprint(glpi.test())
