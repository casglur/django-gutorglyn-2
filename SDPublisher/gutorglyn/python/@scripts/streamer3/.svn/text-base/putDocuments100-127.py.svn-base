from bsddb3.db import *
from dbxml import *
from django.utils.encoding import smart_str

#Load source files 001 - 009

sourceDir = '/SDPublisher/SDPublisher/gutorglyn/texts/'

#fileRange = range(1,10)
#
#for x in fileRange:
#    mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
#    mycontainer = mymgr.openContainer("/SDPublisher/SDPublisher/gutorglyn/gutorglyn.bdbxml")    
#    xmlucontext = mymgr.createUpdateContext()    
#    xmlinput = mymgr.createLocalFileInputStream(sourceDir + "guto00" + str(x) + ".xml")    
#    mycontainer.putDocument("guto00" + str(x) + ".xml", xmlinput, xmlucontext)
#    print 'Added: ' + str(x)
#    
#    del xmlucontext 
#    del mycontainer
#    
#print '1 - 9 Added'
#    
#    
##Load source files 010 - 099
#
#fileRange = range(10,100)
#
#for x in fileRange:
#    mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
#    mycontainer = mymgr.openContainer("/SDPublisher/SDPublisher/gutorglyn/gutorglyn.bdbxml")     
#    xmlucontext = mymgr.createUpdateContext()    
#    xmlinput = mymgr.createLocalFileInputStream(sourceDir + "guto0" + str(x) + ".xml")    
#    mycontainer.putDocument("guto0" + str(x) + ".xml", xmlinput, xmlucontext)
#    print 'Added: ' + str(x)  
#     
#    del xmlucontext 
#    del mycontainer       
#
#print '10-99 Added'

#Load source files 100 - 126

fileRange = range(100,127)

for x in fileRange:
    mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
    mycontainer = mymgr.openContainer("/SDPublisher/SDPublisher/gutorglyn/gutorglyn.bdbxml")    
    xmlucontext = mymgr.createUpdateContext()    
    xmlinput = mymgr.createLocalFileInputStream(sourceDir + "guto" + str(x) + ".xml")    
    mycontainer.putDocument("guto" + str(x) + ".xml", xmlinput, xmlucontext)    
    print 'Added: ' + str(x)  

    del xmlucontext 
    del mycontainer
    
print '100 - 127 Added'

    
#fileRange = ['18a','20a','44a','46a','46b', '65a', '68a','68b']
#
#for x in fileRange:
#    mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
#    mycontainer = mymgr.openContainer("/SDPublisher/SDPublisher/gutorglyn/gutorglyn.bdbxml")    
#    xmlucontext = mymgr.createUpdateContext()    
#    xmlinput = mymgr.createLocalFileInputStream(sourceDir + "guto0" + str(x) + ".xml")    
#    mycontainer.putDocument("guto0" + str(x) + ".xml", xmlinput, xmlucontext)    
#    print 'Added: ' + str(x)  
#
#    del xmlucontext 
#    del mycontainer
#    
#print str(fileRange) + ' added'
#
#    
#fileRange = ['101a']
#
#for x in fileRange:
#    mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
#    mycontainer = mymgr.openContainer("/SDPublisher/SDPublisher/gutorglyn/gutorglyn.bdbxml")    
#    xmlucontext = mymgr.createUpdateContext()    
#    xmlinput = mymgr.createLocalFileInputStream(sourceDir + "guto" + str(x) + ".xml")    
#    mycontainer.putDocument("guto" + str(x) + ".xml", xmlinput, xmlucontext)   
#    print 'Added: ' + str(x)   
#    
#    del xmlucontext 
#    del mycontainer
#    
#print str(fileRange) + ' Added'
#
#fileRange = ['pobl']
#
#for x in fileRange:
#    mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
#    mycontainer = mymgr.openContainer("/SDPublisher/SDPublisher/gutorglyn/gutorglyn.bdbxml")    
#    xmlucontext = mymgr.createUpdateContext()    
#    xmlinput = mymgr.createLocalFileInputStream(sourceDir + str(x) + ".xml")    
#    mycontainer.putDocument("guto" + str(x) + ".xml", xmlinput, xmlucontext)   
#    print 'Added: ' + str(x)   
#
#    del xmlucontext 
#    del mycontainer  
#    
#print str(fileRange) + ' Added'

print 'All done!'

      
