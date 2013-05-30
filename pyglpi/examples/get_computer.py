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
        username = os.environ['GLPI_USERNAME']
    except:
        warnings.warn("GLPI environment variables not locally set", RuntimeWarning)
        host = raw_input("Enter your GLPI hostname: ")
        username = raw_input("Enter your GLPI username: ")

    password = getpass.getpass("Enter your password: ")
    glpi = GLPIClient.RESTClient()
    # my servers are configured with the glpi root under VirtualHost
    # configurations, BASEURL changed accordingly on next line.
    glpi.BASEURL = ''
    glpi.SCHEME = 'https://'
    glpi.connect(host,username,password)

    print "\nGetting Computer\n"
    pprint.pprint(glpi.get_computer(29))

    print "\nGetting Help\n"
    pprint.pprint(glpi.get_computer(29,help=True))

    print "\nGetting Computer With All Options\n"
    pprint.pprint(glpi.get_computer(29, id2name=True,
                                    networkports=True, contracts=True ))

    print "\nGetting with infocoms doesn't work for some reason, skipping\n"

    # pprint.pprint(glpi.get_computer(29, id2name=True,
    #                                 networkports=True, contracts=True,
    #                                 infocoms=True))
