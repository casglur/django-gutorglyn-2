from bsddb3.db import *
from dbxml import *
from django.utils.encoding import smart_str

#Load source files 001 - 009

sourceDir = '../../../texts/'
dbDir = 'C:\Users\lsrobert\Documents\shared work\external work\gutorGlyn\SDPublisher\gutorglyn'
fileRange = range(1,10)

for x in fileRange:
    environment = DBEnv()
    environment.open(dbDir,
        DB_CREATE|DB_INIT_LOCK|DB_INIT_LOG|DB_INIT_MPOOL|DB_INIT_TXN, 0)
    mymgr = XmlManager(environment, DBXML_ALLOW_EXTERNAL_ACCESS)
    xmlinput = mymgr.createLocalFileInputStream(sourceDir + "guto00" + str(x) + ".xml")    
    uc = mymgr.createUpdateContext()
    container = mymgr.openContainer("gutorglyn.bdbxml", DBXML_TRANSACTIONAL)
    txn = mymgr.createTransaction()
    container.putDocument("guto00" + str(x) + ".xml", xmlinput, uc)
    txn.commit()
    print 'Added: ' + str(x) 
    
    del txn
    del uc
    del container    
    
print '1 - 9 Added'
    
    
#Load source files 010 - 099

fileRange = range(10,100)

for x in fileRange:
    xmlinput = mymgr.createLocalFileInputStream(sourceDir + "guto0" + str(x) + ".xml")    
    uc = mymgr.createUpdateContext()
    container = mymgr.openContainer("gutorglyn.bdbxml", DBXML_TRANSACTIONAL)
    txn = mymgr.createTransaction()
    container.putDocument("guto0" + str(x) + ".xml", xmlinput, uc)
    txn.commit()
    
    del txn
    del uc
    del container        

print '10-99 Added'

#Load source files 100 - 126

fileRange = range(100,127)

for x in fileRange:
    xmlinput = mymgr.createLocalFileInputStream(sourceDir + "guto" + str(x) + ".xml")    
    uc = mymgr.createUpdateContext()
    container = mymgr.openContainer("gutorglyn.bdbxml", DBXML_TRANSACTIONAL)
    txn = mymgr.createTransaction()
    container.putDocument("guto" + str(x) + ".xml", xmlinput, uc)
    txn.commit()
    print 'Added: ' + str(x) 
   
    del txn
    del uc
    del container 
    
print '100 - 127 Added'

    
fileRange = ['18a','20a','44a','46a','46b', '65a', '68a','68b']

for x in fileRange:
    xmlinput = mymgr.createLocalFileInputStream(sourceDir + "guto0" + str(x) + ".xml")    
    uc = mymgr.createUpdateContext()
    container = mymgr.openContainer("gutorglyn.bdbxml", DBXML_TRANSACTIONAL)
    txn = mymgr.createTransaction()
    container.putDocument("guto0" + str(x) + ".xml", xmlinput, uc)
    txn.commit()
    print 'Added: ' + str(x) 
    
    del txn
    del uc    
    del container 
    
print str(fileRange) + ' added'

    
fileRange = ['101a']

for x in fileRange:
    xmlinput = mymgr.createLocalFileInputStream(sourceDir + "guto" + str(x) + ".xml")    
    uc = mymgr.createUpdateContext()
    container = mymgr.openContainer("gutorglyn.bdbxml", DBXML_TRANSACTIONAL)
    txn = mymgr.createTransaction()
    container.putDocument("guto" + str(x) + ".xml", xmlinput, uc)
    txn.commit()
    print 'Added: ' + str(x) 

    del txn
    del uc    
    del container 
    
print str(fileRange) + ' Added'

fileRange = ['pobl']

for x in fileRange:
    xmlinput = mymgr.createLocalFileInputStream(sourceDir + str(x) + ".xml") 
    uc = mymgr.createUpdateContext()
    container = mymgr.openContainer("gutorglyn.bdbxml", DBXML_TRANSACTIONAL)
    txn = mymgr.createTransaction()
    container.putDocument(str(x) + ".xml", xmlinput, uc)
    txn.commit()
    print 'Added: ' + str(x) 
    
    del txn
    del uc    
    del container 
    
print str(fileRange) + ' Added'

print 'All done!'

      
