from bsddb3.db import *
from dbxml import *
from django.utils.encoding import smart_str



fileRange = ['18a','20a','44a','46a','46b', '65a', '68a','68b']

for x in fileRange:
    mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
    mycontainer = mymgr.openContainer("..//gutorglyn.bdbxml")    
    xmlucontext = mymgr.createUpdateContext()    
    xmlinput = mymgr.createLocalFileInputStream("C:/Users/lsrobert/Documents/shared work/external work/gutorGlyn/XML/edited_texts/April 2012/POEMS 30MARCH/guto0" + str(x) + ".xml")    
    mycontainer.putDocument("guto0" + str(x) + ".xml", xmlinput, xmlucontext)    
    del mycontainer
    
    
fileRange = ['101a']

for x in fileRange:
    mymgr = XmlManager(DBXML_ALLOW_EXTERNAL_ACCESS)
    mycontainer = mymgr.openContainer("..//gutorglyn.bdbxml")    
    xmlucontext = mymgr.createUpdateContext()    
    xmlinput = mymgr.createLocalFileInputStream("C:/Users/lsrobert/Documents/shared work/external work/gutorGlyn/XML/edited_texts/April 2012/POEMS 30MARCH/guto" + str(x) + ".xml")    
    mycontainer.putDocument("guto" + str(x) + ".xml", xmlinput, xmlucontext)    
    del mycontainer