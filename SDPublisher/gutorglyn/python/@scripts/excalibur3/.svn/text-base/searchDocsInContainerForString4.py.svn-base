from bsddb3.db import *
from dbxml import *

#python implementation of C++ code at BDBXML Figure. 9-10 with Eager and Lazy Evaluation
myManager = XmlManager()    #XmlManager
myContainer = myManager.openContainer("../gutorglyn.bdbxml")    #XmlContainer
myContext = myManager.createQueryContext()  #XmlQueryContext
myContext.setEvaluationType(XmlQueryContext.Eager)
myQuery = r"for $lines in collection('../gutorglyn.bdbxml')//div[@type='lev1']/lg/l where some $line in $lines satisfies (contains($line, 'gwen')) return $lines"
results = myManager.query(myQuery, myContext) #XmlResults

count = 0
newlist = []
for value in results:
    document = value.asDocument()
    name = document.getName()
    content = value.asString()
    count +=1
    newlist.append(content)
    print str(count) + content

print newlist  

del myContainer