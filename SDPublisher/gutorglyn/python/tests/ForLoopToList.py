# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *
'''
Created on 29 April 2013

@author: lsrobert
'''
mgr = XmlManager()
container = mgr.openContainer("../../../gutorglyn/gutorglyn.bdbxml")
results = container.getAllDocuments(0)
print dir(results)

myList = []

for value in results:
    doc = value.asDocument()
    docs = doc.getName()
    myList.append(docs)

print myList

mainlist = []
for i in range(10):
    a = 'name_'
    b = str(i)
    c = a+b
    c = [i]
    mainlist.append((a+b)+'_st00f')
print(mainlist)    