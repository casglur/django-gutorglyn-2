from bsddb3.db import *
from dbxml import *
from django.utils.encoding import smart_str

sourceDir = '../../texts/'

filename = 'pobl.xml'

environment = DBEnv()
environment.open("C:\Users\lsrobert\Documents\shared work\external work\gutorGlyn\SDPublisher\gutorglyn",
    DB_CREATE|DB_INIT_LOCK|DB_INIT_LOG|DB_INIT_MPOOL|DB_INIT_TXN, 0)
mymgr = XmlManager(environment, DBXML_ALLOW_EXTERNAL_ACCESS)
container = mymgr.openContainer("gutorglyn.bdbxml", DBXML_TRANSACTIONAL)
xmlinput = mymgr.createLocalFileInputStream(sourceDir + str(filename)) 
uc = mymgr.createUpdateContext()
txn = mymgr.createTransaction()
container.putDocument(txn, str(filename), xmlinput, uc)
txn.commit()

del container


