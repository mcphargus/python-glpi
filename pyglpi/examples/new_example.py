import sys, os
sys.path.insert(0,os.path.abspath('..'))

from GLPI.GLPIObject import Ticket
from GLPI.GLPIObject import User
from GLPI.GLPIObject import InventoryItem
from GLPI.GLPIObject import Computer
from GLPI.GLPIObject import Document
from GLPI import GLPIClient

inv_item = InventoryItem()
ticket = Ticket()
user = User()
user.object_id = 12
print user.object_id
user.name = "Clint Grimsley"
document = Document()
print document.title
print user.name
