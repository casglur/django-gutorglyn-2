from bsddb3.db import *
from dbxml import *
from django.utils.encoding import smart_str

#Load source files 001 - 009

sourceDir = '../../../texts/'
container = '../../../gutorglyn.bdbxml'


fileRange = range(1,10)
filePrefix = 'guto00'

for x in fileRange:
    mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
    mycontainer = mymgr.openContainer(container)    
    xmlucontext = mymgr.createUpdateContext()    
    xmlinput = mymgr.createLocalFileInputStream(sourceDir + filePrefix + str(x) + ".xml")    
    mycontainer.putDocument(filePrefix + str(x) + ".xml", xmlinput, xmlucontext)
    print 'Added: ' + str(x)   
    del mycontainer
    
print '1 - 9 Added'
    
    
#Load source files 010 - 099

fileRange = range(10,100)
filePrefix = 'guto0'

for x in fileRange:
    mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
    mycontainer = mymgr.openContainer(container)     
    xmlucontext = mymgr.createUpdateContext()    
    xmlinput = mymgr.createLocalFileInputStream(sourceDir + filePrefix + str(x) + ".xml")    
    mycontainer.putDocument(filePrefix + str(x) + ".xml", xmlinput, xmlucontext)
    print 'Added: ' + str(x)   
    del mycontainer        

print '10-99 Added'

#Load source files 100 - 126

fileRange = range(100,127)
filePrefix = 'guto'

for x in fileRange:
    mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
    mycontainer = mymgr.openContainer(container)    
    xmlucontext = mymgr.createUpdateContext()    
    xmlinput = mymgr.createLocalFileInputStream(sourceDir + filePrefix + str(x) + ".xml")    
    mycontainer.putDocument(filePrefix + str(x) + ".xml", xmlinput, xmlucontext)    
    print 'Added: ' + str(x)  
    del mycontainer
    
print '100 - 127 Added'

    
fileRange = ['18a','20a','44a','46a','46b', '65a', '68a','68b']
filePrefix = 'guto0'

for x in fileRange:
    mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
    mycontainer = mymgr.openContainer(container)    
    xmlucontext = mymgr.createUpdateContext()    
    xmlinput = mymgr.createLocalFileInputStream(sourceDir + filePrefix + str(x) + ".xml")    
    mycontainer.putDocument(filePrefix + str(x) + ".xml", xmlinput, xmlucontext)    
    print 'Added: ' + str(x)  
    del mycontainer
    
print str(fileRange) + ' added'

    
fileRange = ['101a']
filePrefix = 'guto'

for x in fileRange:
    mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
    mycontainer = mymgr.openContainer(container)    
    xmlucontext = mymgr.createUpdateContext()    
    xmlinput = mymgr.createLocalFileInputStream(sourceDir + filePrefix + str(x) + ".xml")    
    mycontainer.putDocument(filePrefix + str(x) + ".xml", xmlinput, xmlucontext)   
    print 'Added: ' + str(x)   
    del mycontainer  
    
print str(fileRange) + ' Added'

# fileRange = ['pobl']
# 
# for x in fileRange:
#     mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
#     mycontainer = mymgr.openContainer(container)    
#     xmlucontext = mymgr.createUpdateContext()    
#     xmlinput = mymgr.createLocalFileInputStream(sourceDir + str(x) + ".xml")    
#     mycontainer.putDocument(str(x) + ".xml", xmlinput, xmlucontext)   
#     print 'Added: ' + str(x)   
#     del mycontainer  
#     
# print str(fileRange) + ' Added'

print 'All done!'

      
