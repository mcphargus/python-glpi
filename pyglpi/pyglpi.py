#!/usr/bin/env python

"""
@author: Clint Grimsley
@license: GPLv2 U{http://www.gnu.org/licenses/gpl-2.0.html}

"""



import urllib, urllib2
import json
import gzip
import pprint
import sys

class GLPI:
    """
    
    This is a python interface to the U{GLPI webservices plugin
    <http://plugins.glpi-project.org/spip.php?article94>} It depends
    heavily on JSON, urllib and urllib2. Requires python 2.7. Also,
    has only been tested with v.1.3.0 of the GLPI webservices plugin.

    All types are run through urllib2.urlencoder, so the get coerced
    into strings, but the types the REST API expects are delineated
    anyway.

    This documentation, with few ammendments, has been lifted (without
    permission) almost ver batim from
    U{https://forge.indepnet.net/projects/webservices/wiki/En_devguide}.

    Thanks so much to all the awesome developers that have made the
    webservices plugin and GLPI so useful.
    """
    
    def __init__(self):        
        pass
        
    def __request__(self,params):
        return self.url + urllib.urlencode(params)

    def connect(self,host,login_name,login_password):
        """
        Connect to a running GLPI instance that has the webservices
        plugin enabled. U{It's available here
        <http://plugins.glpi-project.org/spip.php?article94>}

        @type host: FQDN string
        @param host: hostname of the GLPI server, has not been tested
        with HTTPS
        @type login_name: string
        @param login_name: your GLPI username
        @type login_password: string
        @param login_password: pretty obvious
        """
        self.url = 'http://'+host+'/plugins/webservices/rest.php?'
        self.login_name = login_name
        self.login_password = login_password
        params = {'login_name':login_name,
                  'login_password':login_password,
                  'method':'glpi.doLogin'}
        request = urllib2.Request(self.url + urllib.urlencode(params))
        response = urllib2.urlopen(request).read()
        session_id = json.loads(response)['session']
        self.session = session_id

    def get_server_status(self):
        """
        Gets server status information from the GLPI server, mostly
        stating that things are OK.
        """
        params = {'method':'glpi.status',
                  'session':self.session}
        request = urllib2.Request(self.url + urllib.urlencode(params))
        response = urllib2.urlopen(request).read()
        return json.loads(response)

    """
    User context methods
    """

    def get_my_info(self):
        """
        Returns JSON serialized information about the currently logged
        in user.
        """
        params = {'method':'glpi.getMyInfo',
                  'session':self.session}
        response = urllib2.urlopen(self.__request__(params))
        return json.loads(response.read())

    def list_my_profiles(self):
        """
        Returns JSON serialized profile information about the
        currently logged in user.
        """
        params = {'method':'glpi.listMyProfiles',
                  'session':self.session}
        response = urllib2.urlopen(self.__request__(params))
        return json.loads(response.read())

    def list_my_entities(self):
        """
        Returns JSON serialized informations about the entities of the
        currently logged in user.
        """
        params = {'method':'glpi.listMyEntities',
                  'session':self.session}
        response = urllib2.urlopen(self.__request__(params))
        return json.loads(response.read())

    """
    Information retrieval methods
    """

    def get_ticket(self,ticket_id,id2name=None,_help=None):
        """
        Retrieve a ticket from the GLPI server. Returns a JSON
        serialized ticket

        @type ticket_id: integer
        @param ticket_id: ID of the ticket being requested
        @type id2name: string
        @param id2name: option to enable id to name translation of dropdown fields
        @type _help: boolean
        @param _help: return JSON serialized help about the API call
        """        
        params = {'method':'glpi.getTicket',
                  'ticket':ticket_id,
                  'session':self.session}
        if id2name: params['id2name'] = str(id2name)
        if _help: params['help'] = help

        response = urllib2.urlopen(self.__request__(params))
        return json.loads(response.read())

    def get_object(self,itemtype,_id,show_label=None,
                     show_name=None,_help=None):
        """
        Returns a JSON object from the GLPI server. itemtype can take
        one of the following:
        U{https://forge.indepnet.net/embedded/glpi/annotated.html}

        @type itemtype: integer
        @param itemtype: type of the item being requested
        @type _id:integer
        @param _id: primary key of the item being requested
        @type show_label: boolean
        @param show_label: show label
        @type show_name: boolean
        @param show_name: show name
        @type _help: boolean
        @param _help: list available options in JSON
        """
        params = {'method':'glpi.getObject',
                  'session':self.session}
        
        if itemtype: params['itemtype'] = itemtype
        if _id: params['id'] = _id
        if show_label: params['show_label'] = show_label
        if show_name: params['show_name'] = show_name
        if _help: params['help'] = _help
        response = urllib2.urlopen(self.__request__(params))
        return json.loads(response.read())

    def get_computer(self,computer,id2name=None,infocoms=None,contracts=None,networkports=None,_help=None):
        """
        Returns a JSON serialized computer object from the GLPI server

        @type computer: integer
        @param computer: computerID
        
        @type id2name: boolean
        @param id2name: option to enable id to name translation of dropdown fields
        @type infocoms: boolean
        @param infocoms: return infocoms associated with the computer
        @type contracts: boolean
        @param contracts: return contracts associated with the computer
        @type networkports: boolean
        @param networkports: return information about computer's network ports
        @type _help: boolean
        @param _help: returns a serialized object representing help about how to use this method
        """

        params = {'method':'glpi.getComputer',
                  'session': self.session,
                  'computer':computer}
        if id2name: params['id2name'] = id2name
        if infocoms: params['infocoms'] = infocoms
        if contracts: params['contracts'] = contracts
        if networkports: params['networkports'] = networkports
        if _help: params['help'] = _help

        response = urllib2.urlopen(self.__request__(params))
        return json.loads(response.read())

    def get_computer_infocoms(self):
        """
        Return a JSON serialized list of computer infocoms from the
        GLPI server.        
        """
        pass

    def get_computer_contracts(self):
        """
        Return a JSON serialized list of computer contracts from the
        GLPI server.
        """
        pass

    def get_networking_equipment(self):
        """
        Return a JSON serialized list of networking gear from the GLPI
        server.
        """
        pass

    def get_infocoms(self):
        """
        Return a JSON serialized list of infocoms from the GLPI
        server.
        """
        pass

    def get_contracts(self):
        """
        Return a JSON serialized list of contracts from the GLPI server.
        """
        pass

    def get_network_ports(self):
        """
        Return a JSON serialized list of network ports from the GLPI
        server.
        """
        pass

    def list_computers(self):
        """
        Return a JSON serialized list of computers from the GLPI
        server.        
        """
        pass

    def list_dropdown_menus(self):
        """
        Return a JSON serialized list of dropdown menus from the GLPI
        server.
        """
        pass

    def list_groups(self):
        """
        Return a JSON serialized list of groups from the GLPI server.
        """
        pass

    def list_helpdesk_items(self):
        """
        Return a JSON serialized list of helpdesk items from the GLPI
        server.
        """
        pass

    def list_helpdesk_types(self):
        """
        Return a JSON serialized list of helpdesk types from the GLPI
        server.
        """
        pass

    def list_inventory_objects(self):
        """
        Return a JSON serialized list of inventory objects from the
        GLPI server.
        """
        pass

    def list_objects(self):
        """
        Return as JSON serialized list of objects from the GLPI server.
        """
        pass

    def list_tickets(self):
        """
        Return a JSON serialized list of tickets from the GLPI server.
        """
        pass

    def list_users(self):
        """
        Return a JSON serialized list of users from the GLPI server.
        """
        
        params = {'method':'glpi.listUsers',
                  'session':self.session}
        response = urllib2.urlopen(self.__request__(params))
        return json.loads(response.read())

    """
    Action methods
    """

    def create_ticket(self,title,content,entity=None,user=None,group=None,requester=None,
                      victim=None,observer=None,date=None,itemtype=None,item=None,
                      urgency=None,_type=None,source=None,category=None,user_email=None,
                      user_email_notification=None,_help=None):

        """
        Returns a JSON serialized version of a ticket upon
        success. Unless otherwise noted, all params are optional
        
        @type entity: integer
        @param entity: ID, optional, default is current on, must be in the active ones
        @type user: integer or list of integers
        @param user: requester ID, default to current logged in user
        @type group: integer or list of integers
        @param group: requester ID, default is None
        @type requester: integer or list of integers
        @param requester: additional requester(s) with mail notification
        @type victim: integer or list of integers
        @param victim: same as requester, without mail notification
        @type observer: integer or list of integers
        @param observer: additional observers
        @type date: ISO formatted date string
        @param date: defaults to system date
        @type itemtype: integer
        @param itemtype: id of the type of the item, optional, default none
        @type item: integer
        @param item: ID of the item, optional, default none
        @type title: string
        @param title: B{required} short description of the issue
        @type content: string
        @param content: B{required} longer description of the issue
        @type urgency: integer
        @param urgency: defaults to 3, 1-5 are accepted
        @type _type: integer
        @param _type: type of ticket, defaults to 1
        @type source: string
        @param source: name of the RequestType, optional, defaults WebServices
        @type category: integer
        @param category: default is none
        @type user_email: string
        @param user_email: enable notification to this email address
        @type user_email_notification: boolean
        @param user_email_notification: enable notification to the users email (if known)
        @type _help: boolean
        @param _help: list available options in JSON
        """

        params = {'method':'glpi.createTicket',
                  'session':self.session,
                  'title':title,
                  'content':content}
        if entity: params['entity'] = entity
        if user: params['user'] = user
        if group: params['group'] = group
        if requester: params['requester'] = requester
        if victim: params['victim'] = victim
        if observer: params['observer'] = observer
        if date: params['date'] = date
        if itemtype: params['itemtype'] = itemtype
        if item: params['item'] = item
        if urgency: params['urgency'] = urgency
        if _type: params['type'] = _type
        if source: params['source'] = source
        if category: params['category'] = category
        if user_email: params['user_email'] = user_email
        if user_email_notification: params['user_email_notification'] = user_email_notification
        if help: params['help'] = _help
        
        response = urllib2.urlopen(self.__request__(params))
        return json.loads(response.read())

    def add_ticket_document(self):
        pass

    def add_ticket_followup(self):
        pass

    def add_ticket_observer(self):
        pass

    def set_ticket_satisfaction(self):
        pass

    def set_ticket_validation(self):
        pass

    def create_objects(self):
        pass

    def delete_objects(self):
        pass

    def update_objects(self):
        pass

    def link_objects(self):
        pass

if __name__ == '__main__':
    username = raw_input("Enter your GLPI username: ")
    password = raw_input("Enter your password: ")    
    glpi = GLPI()
    glpi.connect('glpi.drivefactor.com',username,password)    
