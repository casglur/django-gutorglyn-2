from bsddb3.db import *
from dbxml import *
from django.utils.encoding import smart_str

sourceDir = '../../../texts/'

# filename = 'pobl.xml'
filename = raw_input('Enter a file name: ')

mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
mycontainer = mymgr.openContainer("../../../gutorglyn.bdbxml")    
xmlucontext = mymgr.createUpdateContext()    
xmlinput = mymgr.createLocalFileInputStream(sourceDir + str(filename))    
mycontainer.putDocument(str(filename), xmlinput, xmlucontext)
print str(filename) + ' now added!'   
del mycontainer