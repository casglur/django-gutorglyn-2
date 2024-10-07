from bsddb3.db import *
from dbxml import *
from django.utils.encoding import smart_str

#Load source files 001 - 009

sourceDir = '/SDPublisher/SDPublisher/gutorglyn/texts/'
dbDir = '/SDPublisher/SDPublisher/gutorglyn'
fileRange = range(10,60)
textPrefix = 'guto0'

for x in fileRange:
    environment = DBEnv()
    environment.open(dbDir,
        DB_CREATE|DB_INIT_LOCK|DB_INIT_LOG|DB_INIT_MPOOL|DB_INIT_TXN, 0)
    mymgr = XmlManager(environment, DBXML_ALLOW_EXTERNAL_ACCESS)
    xmlinput = mymgr.createLocalFileInputStream(sourceDir + textPrefix + str(x) + ".xml")    
    uc = mymgr.createUpdateContext()
    container = mymgr.openContainer("gutorglyn.bdbxml", DBXML_TRANSACTIONAL)
    txn = mymgr.createTransaction()
    container.putDocument(textPrefix + str(x) + ".xml", xmlinput, uc)
    txn.commit()
    print 'Added: ' + str(x) 
    
    del uc
    del container    
    
print str(fileRange) + ' Added'
    
print 'All done!'

      
