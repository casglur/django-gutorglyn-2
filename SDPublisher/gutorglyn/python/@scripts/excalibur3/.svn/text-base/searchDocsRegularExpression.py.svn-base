# -*- coding: utf-8 -*-
from django.utils.encoding import smart_str
from bsddb3.db import *
from dbxml import *

mymgr = XmlManager()
# myquery = r"collection('../../../gutorglyn.bdbxml')//tei:note[@xml:id='e_001_027']/tei:p"

searchStr1 = "\Wond\W"
searchStr2 = "\WDafydd\W"
searchStr3 = "\Wa'n\W"
searchStr4 = "\Wgwyr\W"
searchStr5 = "brawd"

searchStr = searchStr1.encode('ascii', 'xmlcharrefreplace')
searchStr = searchStr.replace("'", "’")

# poem_nodes = 'collection("../../../gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[1]/tei:lg/tei:l'
# pageStart = "0" 
# pageEnd = "10"
# regExCaseFlag = "i"

myquery= ('\
     declare variable $query := "%s"; \
     declare variable $poem_nodes as node()* := collection("../../../gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[1]/tei:lg/tei:l; \
     let $start := 0 \
     let $end := 100 \
     for $x at $i in $poem_nodes[matches(., $query, "")] \
     return $x[$i = ($start to $end)] \
     ' % (smart_str(searchStr5)))

print myquery

mycontainer = mymgr.openContainer("../../../gutorglyn.bdbxml")
qcontext = mymgr.createQueryContext()
qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")

qcontext.setDefaultCollection("../../../gutorglyn.bdbxml")

queryexp = mymgr.prepare(myquery, qcontext)

results = queryexp.execute(qcontext)

count = 0

for value in results:
    document = value.asDocument()
    name = document.getName()
    content = value.asString()
    count +=1

    print str(count), name, ": ", content
    
del mycontainer
