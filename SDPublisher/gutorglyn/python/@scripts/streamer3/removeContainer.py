
from bsddb3.db import *
from dbxml import *


dbName = 'gutorglyn.bdbxml'

mymgr = XmlManager()
mycontainer = mymgr.removeContainer("/SDPublisher/SDPublisher/gutorglyn/" + dbName)

del mycontainer
print 'Container removed!'