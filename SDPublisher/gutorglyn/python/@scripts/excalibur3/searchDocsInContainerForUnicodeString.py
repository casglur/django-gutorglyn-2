# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *

myTerm = 'Gŵr'
#myTerm = u'G\u0174r'
#python implementation of C++ code at BDBXML Figure. 9-10 with Eager and Lazy Evaluation
myManager = XmlManager()    #XmlManager
myContainer = myManager.openContainer("../../../gutorglyn.bdbxml")    #XmlContainer
myContext = myManager.createQueryContext()  #XmlQueryContext
myContext.setEvaluationType(XmlQueryContext.Eager) #Set EvaluationType to Eager to match Pixelise default
myQuery = 'for $lines in collection(\'../../../gutorglyn.bdbxml\')//div[@type=\'lev1\']/lg/l where some $line in $lines satisfies (contains($line, \'%(myTerm)s\')) return $lines'  % {'myTerm': myTerm}
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
    newdict[name] = content
    print name + str(count) + content

newlist = [newdict]

print 'Number of results: ' + str(count)
print 'Query: ' + str(myQuery)
print 'Search term is type: ' + str(type(myTerm))
print 'List = ' +str(newlist)
print 'Dict = ' +str(newdict)

del myContainer
