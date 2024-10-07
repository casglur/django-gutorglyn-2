
from bsddb3.db import *
from dbxml import *

myenv = DBEnv()
myenv.set_cachesize(0, 50000000, 1)
myenv.open("C:/Users/lsrobert/Documents/shared work/external work/gutorGlyn/SDPublisher/gutorglyn", DB_CREATE|DB_INIT_LOCK|DB_INIT_LOG|DB_INIT_MPOOL|DB_INIT_TXN|DB_RECOVER, 0)
mymgr = XmlManager(myenv, 0)
mycontainer = mymgr.createContainer("C:/Users/lsrobert/Documents/shared work/external work/gutorGlyn/SDPublisher/gutorglyn/gutorglyn.bdbxml", DBXML_TRANSACTIONAL)

del mycontainer
myenv.close(0)

print 'Success!'
