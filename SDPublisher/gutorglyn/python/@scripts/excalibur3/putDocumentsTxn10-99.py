from bsddb3.db import *
from dbxml import *
from django.utils.encoding import smart_str

#Load source files 001 - 009

sourceDir = '../../texts/'
#fileRange = range(1,10)
#fileRange = range(10,20)
#fileRange = range(30,40)
#fileRange = range(40,50)
fileRange = range(10,60)

environment = DBEnv()
environment.set_lk_detect(DB_LOCK_MINWRITE)
environment.set_lk_max_lockers(2000)
environment.set_lk_max_locks(2000)
environment.set_lk_max_objects(2000)
environment.set_tx_max(100)
environment.set_cachesize(0, 64 * 1024 * 1024, 1)
environment.mutex_set_max(5000)
environment.open("C:\Users\lsrobert\Documents\shared work\external work\gutorGlyn\SDPublisher\gutorglyn",
    DB_CREATE|DB_INIT_LOCK|DB_INIT_LOG|DB_INIT_MPOOL|DB_INIT_TXN, 0)
environment.txn_checkpoint()
mymgr = XmlManager(environment, DBXML_ALLOW_EXTERNAL_ACCESS)
mymgr.setDefaultPageSize(64000)
uc = mymgr.createUpdateContext()


for x in fileRange:

#    xmlinput = mymgr.createLocalFileInputStream(sourceDir + "guto00" + str(x) + ".xml") 
    xmlinput = mymgr.createLocalFileInputStream(sourceDir + "guto0" + str(x) + ".xml")   
    txn = mymgr.createTransaction()
    container = mymgr.openContainer("gutorglyn.bdbxml", DBXML_TRANSACTIONAL)
    container.putDocument("", xmlinput, uc, DBXML_GEN_NAME)
    txn.commit()
    print 'Added: ' + str(x) 
    
    container.close()
    del container

environment.close()   
    
#print '1-10 Added'
#print '10-20 Added'
#print '20-30 Added'
#print '30-40 Added'
#print '40-50 Added'
print '10-60 Added'


print 'All done!'

      
