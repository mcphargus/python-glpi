#!/usr/bin/env python
#-*- coding:utf-8 -*-

class GLPIObject(object):
    """
    Base class for all GLPI objects

    :type object_id: int
    :type entities_id: int
    :type object_url: string
    :type itemtype: string
    :type name: string

    :param object_id: object identifier
    :param entities_id: entity identifier
    :param object_url: url of object
    :param itemtype: type of object
    :param name: name of object
    """

    object_id = None
    entities_id = None
    object_url = None
    itemtype = None
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
    """
    Ticket

    :type actiontime: datetime
    :type begin_waiting_date: datetime
    :type close_delay_stat: int
    :type closedate: datetime
    :type content: string
    :type cost_fixed: float
    :type cost_material: float
    :type cost_time: float
    :type date: datetime
    :type date_mod: datetime
    :type due_date: datetime
    :type entities_id: int
    :type global_validation: string
    :type impact: int
    :type is_deleted: bool
    :type items_id: int
    :type itemtype: string
    :type itilcategories_id: int
    :type name: string
    :type priority: int
    :type requesttypes_id: int
    :type sla_waiting_duration: int
    :type slalevels_id: int
    :type slas_id: int
    :type solution: string
    :type solutiontypes_id: int
    :type solve_delay_stat: int
    :type solvedate: datetime
    :type status: string
    :type suppliers_id_assign: int
    :type takeintoaccount_delay_stat: int
    :type type: int
    :type urgency: int
    :type users_id_lastupdater: int
    :type users_id_recipient: int
    :type waiting_duration: int
    :type users: dict
    :type groups: dict

    :param actiontime: 
    :param begin_waiting_date: 
    :param close_delay_stat: 
    :param closedate: 
    :param content: 
    :param cost_fixed: 
    :param cost_material: 
    :param cost_time: 
    :param date: 
    :param date_mod: 
    :param due_date: 
    :param entities_id: 
    :param global_validation: 
    :param impact: 
    :param is_deleted: 
    :param items_id: 
    :param itemtype: 
    :param itilcategories_id: 
    :param name: 
    :param priority: 
    :param requesttypes_id: 
    :param sla_waiting_duration: 
    :param slalevels_id: 
    :param slas_id: 
    :param solution: 
    :param solutiontypes_id: 
    :param solve_delay_stat: 
    :param solvedate: 
    :param status: 
    :param suppliers_id_assign: 
    :param takeintoaccount_delay_stat: 
    :param type: 
    :param urgency: 
    :param users_id_lastupdater: 
    :param users_id_recipient: 
    :param waiting_duration: 
    :param users: 
    :param groups: 

    """

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
    users = None
    groups = None

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
    """
    User

    :type firstname: string
    :type realname: string
    :type email: string
    :type phone: string
    :type locations_id: int
    :type login: string

    :param firstname: firstname
    :param realname: surname
    :param email: email address
    :param phone: phone number
    :param locations_id: location identifier
    :param login: login name
    """
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
    """
    Computer

    :type autoupdatesystems_id: int
    :type autoupdatesystems_name: string
    :type comment: string
    :type computermodels_id: int
    :type computertypes_id: int
    :type contact: int
    :type contact_num: int
    :type contracts: list
    :type date_mod: datetime
    :type domains_id: int
    :type domains_name: string
    :type entities_id: int
    :type groups_id: int
    :type groups_id_tech: int
    :type is_deleted: bool
    :type is_ocs_import: bool
    :type is_template: bool
    :type locations_id: int
    :type manufacturers_id: int
    :type manufacturers_name: string
    :type name: string
    :type networkports: list
    :type networks_id: int
    :type networks_name: string
    :type notepad: string
    :type operatingsystems_id: int
    :type operatingsystemservicepacks_id: int
    :type operatingsystemversions_id: int
    :type os_license_number: string
    :type os_licenseid: string
    :type otherserial: string
    :type serial: string
    :type states_id: int
    :type states_name: string
    :type template_name: string
    :type ticket_tco: float
    :type users_id: int
    :type users_id_tech: int
    :type uuid: string

    :param autoupdatesystems_id:
    :param autoupdatesystems_name:
    :param comment:
    :param computermodels_id:
    :param computertypes_id:
    :param contact:
    :param contact_num:
    :param contracts:
    :param date_mod:
    :param domains_id:
    :param domains_name:
    :param entities_id:
    :param groups_id:
    :param groups_id_tech:
    :param is_deleted:
    :param is_ocs_import:
    :param is_template:
    :param locations_id:
    :param manufacturers_id:
    :param manufacturers_name:
    :param name:
    :param networkports:
    :param networks_id:
    :param networks_name:
    :param notepad:
    :param operatingsystems_id:
    :param operatingsystemservicepacks_id:
    :param operatingsystemversions_id:
    :param os_license_number:
    :param os_licenseid:
    :param otherserial:
    :param serial:
    :param states_id:
    :param states_name:
    :param template_name:
    :param ticket_tco:
    :param users_id:
    :param users_id_tech:
    :param uuid:
    """
    autoupdatesystems_id = None
    autoupdatesystems_name = None
    comment = None
    computermodels_id = None
    computertypes_id = None
    contact = None
    contact_num = None
    contracts = None
    date_mod = None
    domains_id = None
    domains_name = None
    entities_id = None
    groups_id = None
    groups_id_tech = None
    is_deleted = None
    is_ocs_import = None
    is_template = None
    locations_id = None
    manufacturers_id = None
    manufacturers_name = None
    name = None
    networkports = None
    networks_id = None
    networks_name = None
    notepad = None
    operatingsystems_id = None
    operatingsystemservicepacks_id = None
    operatingsystemversions_id = None
    os_license_number = None
    os_licenseid = None
    otherserial = None
    serial = None
    states_id = None
    states_name = None
    template_name = None
    ticket_tco = None
    users_id = None
    users_id_tech = None
    uuid = None

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
    """
    Document

    .. note:: url and base64 are mutually exclusive

    :type url: string
    :type name: string
    :type base64: base64 encoded string
    :type comment: string
    :type content: string
    :param url: url of the document to be uploaded
    :param name: name of the document
    :param base64: content of the document in base64 encoded string
    :param comment: depracated, use *content* instead
    :param content: if present, also add a followup, if the
      documentation upload succeeded, for additional options, see
      `GLPIClient.add_ticket_followup`
    """
    url = None
    name = None
    comment = None
    base64 = None
    content = None

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
