from bsddb3.db import *
from dbxml import *
from django.utils.encoding import smart_str

#Load source files 001 - 009

sourceDir = '../../texts/'
fileRange = range(1,10)

environment = DBEnv()
environment.open("C:\Users\lsrobert\Documents\shared work\external work\gutorGlyn\SDPublisher\gutorglyn",
    DB_CREATE|DB_INIT_LOCK|DB_INIT_LOG|DB_INIT_MPOOL|DB_INIT_TXN, 0)
mymgr = XmlManager(environment, DBXML_ALLOW_EXTERNAL_ACCESS)
uc = mymgr.createUpdateContext()


for x in fileRange:

    xmlinput = mymgr.createLocalFileInputStream(sourceDir + "*.xml")    
    txn = mymgr.createTransaction()
    container = mymgr.openContainer("gutorglyn.bdbxml", DBXML_TRANSACTIONAL)
    container.putDocument("", xmlinput, uc, DBXML_GEN_NAME)
    txn.commit()
    print 'Added: ' + str(x) 
    
    del container    
    
print '1 - 9 Added'

print 'All done!'

      
