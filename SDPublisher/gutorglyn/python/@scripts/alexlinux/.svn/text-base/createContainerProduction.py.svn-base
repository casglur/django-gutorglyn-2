
from bsddb3.db import *
from dbxml import *

myenv = DBEnv()
myenv.open("C:/SDPublisher/gutorglyn", DB_CREATE|DB_INIT_LOCK|DB_INIT_LOG|DB_INIT_MPOOL|DB_INIT_TXN|DB_RECOVER, 0)
mymgr = XmlManager(myenv, 0)
mycontainer = mymgr.createContainer("C:/SDPublisher/gutorglyn/gutorglyn.bdbxml")

del mycontainer

print 'Container created!'