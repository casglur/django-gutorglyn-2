# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *

#python implementation of C++ code at BDBXML Figure. 9-10 with Eager and Lazy Evaluation
myManager = XmlManager()    #XmlManager
myContainer = myManager.openContainer("../gutorglyn.bdbxml")    #XmlContainer
myContext = myManager.createQueryContext()  #XmlQueryContext
myContext.setEvaluationType(XmlQueryContext.Eager)
myQuery = r"collection('../gutorglyn.bdbxml')//div[@xml:id='Guto008top']/div[@type='lev3']/head/string()"
results = myManager.query(myQuery, myContext) #XmlResults

count = 0
newlist = [] #create new list
newdict = {} #create new dictionary
for value in results:
    content = value.asString()
    count +=1
    newlist.append(content) #append loop value to list
    print str(count) + content

newlist = [newdict]

print str(count)+ ' results returned' 

del myContainer
