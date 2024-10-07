from bsddb3.db import *
from dbxml import *

#python implementation of C++ code at BDBXML Figure. 8-15
myManager = XmlManager()    #XmlManager
myContainer = myManager.openContainer("../gutorglyn.bdbxml")    #XmlContainer
myContext = myManager.createQueryContext()  #XmlQueryContext

myQuery = r"for $lines in collection('../gutorglyn.bdbxml')//div[@type='lev1']/lg/l where some $line in $lines satisfies (contains($line, 'ond')) return $lines"
results = myManager.query(myQuery, myContext) #XmlResults

for value in results:
    document = value.asDocument()
    name = document.getName()
    content = value.asString()

    print name + " - " + content + str(results.size())

del myContainer    