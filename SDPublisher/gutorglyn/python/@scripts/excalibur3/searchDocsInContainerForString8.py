from bsddb3.db import *
from dbxml import *


#python implementation of C++ code at BDBXML Figure. 9-10 with Eager and Lazy Evaluation
myManager = XmlManager()    #XmlManager
myContainer = myManager.openContainer("../../../gutorglyn.bdbxml")    #XmlContainer
myContext = myManager.createQueryContext()  #XmlQueryContext
myContext.setEvaluationType(XmlQueryContext.Eager)
myContext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")
myQuery = r"let $range := (1 to 3) return //tei:div[@xml:id='Guto001testun']/tei:lg/tei:l[@n=$range]"
results = myManager.query(myQuery, myContext) #XmlResults

count = 0
newlist = [] #create new list
newdict = {} #create new dictionary
for value in results:
    document = value.asDocument()
    name = document.getName()
    content = value.asString()
    count +=1
    newlist.append(content) #append loop value to list
    newdict[count] = content
    print str(count) + content

print 'List = ' +str(newlist)
print 'Dict = ' +str(newdict)

del myContainer