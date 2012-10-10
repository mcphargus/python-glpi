#!/usr/bin/env python
#-*- coding:utf-8 -*-

class GLPIObject(object):
    """ Base class for all GLPI objects """
    
    __module__ = "GLPI"
    object_id = None
    entities_id = None
    object_url = None
    name = None
    
    def __init__(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
    def create(self):
        pass
    def list_all(self):
        pass

class InventoryItem(GLPIObject):
    """ InventoryItem """
    
    entities_name = None
    entities_id = None
    serial = None
    otherserial = None
    itemtype = None
    itemtype_name = None

    def __init__(self):
        pass

class Ticket(GLPIObject):
    """ Ticket """

    entities_id = None
    name = None
    date = None
    closedate = None
    solvedate = None
    date_mod = None
    users_id_lastupdater = None
    status = None
    users_id_recipient = None
    requesttypes_id = None
    suppliers_id_assign = None
    itemtype = None
    items_id = None
    content = None
    urgency = None
    impact = None
    priority = None
    ticketcategories_id = None
    _type = None
    cost_time = None
    cost_fixed = None
    cost_material = None
    ticketsolutiontypes_id = None
    solution = None
    global_validation = None
    due_date = None
    begin_waiting_date = None
    sla_waiting_duration = None
    ticket_waiting_duration = None
    close_delay_stat = None
    solve_delay_stat = None
    takeintoaccount_delay_stat = None
    actiontime = None
    slas_id = None
    slalevels_id = None

    def __init__(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
    def create(self):
        pass
    def list_all(self):
        pass


class User(GLPIObject):
    """ User """
    firstname = None
    realname = None
    email = None
    phone = None
    locations_id = None
    login = None

    def __init__(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
    def create(self):
        pass
    def list_all(self):
        pass

class Computer(InventoryItem):
    """ Computer """

    def __init__(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
    def create(self):
        pass
    def list_all(self):
        pass

class Document(GLPIObject):
    """ Document """
    title = None
    def __init__(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
    def create(self):
        pass
    def list_all(self):
        pass
