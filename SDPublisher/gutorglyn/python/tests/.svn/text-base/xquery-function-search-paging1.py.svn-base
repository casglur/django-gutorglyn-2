# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *
from datetime import datetime
from django.utils.encoding import smart_str

# Searches edited texts
#  
userdoc = "collection('../../gutorglyn.bdbxml')/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[1]/tei:lg/tei:l"

# query = raw_input('Enter regular expression: ')

searchStr = "LLawen"

start = 0
end = 40

startTime = datetime.now()

print 'Working on ' + '"%s"...' % searchStr

mymgr = XmlManager()

myquery = ' \
        declare variable $query := "%s"; \
            declare variable $poem_nodes as node()* := %s; \
            declare variable $perpage := 3; \
            let $start := %s \
            let $end := %s \
            for $x at $i in $poem_nodes[dbxml:contains(., $query)] \
            return $x[$i = ($start to $end)] \
            ' % (smart_str(searchStr), userdoc, start, end)


mycontainer = mymgr.openContainer("../../gutorglyn.bdbxml")
qcontext = mymgr.createQueryContext()
qcontext.setDefaultCollection("../gutorglyn.bdbxml")
qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")
qcontext.setEvaluationType(qcontext.Eager)

queryexp = mymgr.prepare(myquery, qcontext)

results = queryexp.execute(qcontext)

count = 0
          
for value in results:
    document = value.asDocument()
    name = document.getName()
    content = value.asString()
    count += 1
    print name + " - " + content
    
print 'Returns ' + str(count) + ' results for ' + '"%s"' % searchStr

del mycontainer

print(datetime.now()-startTime)