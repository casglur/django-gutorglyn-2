# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *
import math

from django.utils.encoding import smart_str

userdoc = "collection('../../gutorglyn.bdbxml')//tei:div[@type='lev1']/tei:lg/tei:l"    

searchStr = 'LLawen'

perPage = int(10)

pageStart = int(30)

if pageStart:
    pageStart = pageStart + 1
    pageEnd = pageStart + perPage - 1
    count = pageStart - 1
else:
    count = 0
    pageStart = 0
    pageEnd = pageStart + perPage  

declareNamespace = 'declare namespace tei="http://www.tei-c.org/ns/1.0";'

searchFunction = 'dbxml:contains(., $query)'
#searchFunction = 'contains(., $query)'
#searchFunction = 'matches(., $query, "i")'

mymgr = XmlManager()
# myquery = r'%s for $lines in collection("../../gutorglyn.bdbxml")//tei:div[@type="lev1"]/tei:lg/tei:l where some $line in $lines satisfies %s return $lines' % (declareNamespace, searchFunction)

myquery = ' \
        declare variable $query := "%s"; \
            declare variable $poem_nodes as node()* := %s; \
            declare variable $perpage := 3; \
            let $pageStart := %s \
            let $pageEnd := %s \
            for $x at $i in $poem_nodes[%s] \
            return $x[$i = ($pageStart to $pageEnd)] \
            ' % (smart_str(searchStr), userdoc, pageStart, pageEnd, searchFunction)
            
            

myCount = 'declare namespace tei="http://www.tei-c.org/ns/1.0"; declare variable $query := "%s"; count(collection("../../gutorglyn.bdbxml")//tei:div[@type="lev1"]/tei:lg/tei:l[%s])' % (searchStr, searchFunction)

mycontainer = mymgr.openContainer("../../gutorglyn.bdbxml")
qcontext = mymgr.createQueryContext()

qcontext.setDefaultCollection("../../gutorglyn.bdbxml")
qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")

queryexp = mymgr.prepare(myquery, qcontext)

queryResults = queryexp.execute(qcontext)

for value in queryResults:
    content = value.asString()
    count += 1
    print str(count) + ' ' + content

queryexp = mymgr.prepare(myCount, qcontext)

countResults = queryexp.execute(qcontext)

for value in countResults:
    countResultsValue = int(value.asString())
    totalPageNum = int(math.ceil(float(countResultsValue)/perPage))
    print 'Occurs in ' + str(countResultsValue ) + ' line(s)'

pageValuesList = []
for i in range(0, totalPageNum * perPage + 1, perPage):
    pageValuesList.append(i)

try:
    currentPageNum = pageValuesList.index(pageEnd)
except:
    currentPageNum = "?"

if countResultsValue < pageEnd:
    pageEnd = countResultsValue


print 'Page ' + str(currentPageNum) + ' of ' + str(totalPageNum) + ' pages'
print 'Page Values are  ' + str(pageValuesList)
print 'pageStart is ' + str(pageStart)
print 'pageEnd is ' + str(pageEnd)
print 'Showing records ' + str(pageStart) + ' to ' + str(pageEnd) + ' of ' + str(countResultsValue)
print 'Search Function: ' + searchFunction
print 'Count Xquery: ' + myCount

del mycontainer
