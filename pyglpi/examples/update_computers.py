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

    # This example of fields comes from deleteObjects doc:
    # https://forge.indepnet.net/projects/webservices/wiki/GlpiupdateObjects
    fields = {
        'Computer': [
            {
            'id': 30,
            'serial': 'J87G-FDZF-970',
            'comment': 'Commentaire 1',
            'otherserial': '000094'
            },
            {
            'id': 31,
            'serial': '544542-029475',
            'comment': 'Commentaire 2',
            'otherserial': '000096'
            },
        ],
        'Monitor': [
            {
            'id': 7,
            'serial': '12133432RE2R2'
            },
            {
            'id': 8,
            'serial': '4234-43-EFZ-434'
            }
        ]
    }
    pprint.pprint(glpi.update_objects(fields))
