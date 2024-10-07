
from bsddb3.db import *
from dbxml import *

dbName = 'gutorglyn.bdbxml'

myenv = DBEnv()
#myenv.set_cachesize(0, 100000000, 1)
myenv.open("/SDPublisher/SDPublisher/gutorglyn", DB_CREATE|DB_INIT_LOG|DB_INIT_MPOOL, 0)
mymgr = XmlManager(myenv, 0)
mycontainer = mymgr.createContainer("/SDPublisher/SDPublisher/gutorglyn/" + dbName)

del mycontainer

print 'Container created!'