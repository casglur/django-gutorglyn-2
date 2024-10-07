
from bsddb3.db import *
from dbxml import *
from datetime import datetime
from django.utils.encoding import smart_str

startTime = datetime.now()

mgr = XmlManager()
# query = "collection('../../gutorglyn.bdbxml')//div[@xml:id='Guto001top']/div[@type='lev3']/lg/l[@n='1']"

search_terms = '(p)ond '
start = 0
end = 10

poem_nodes = 'collection("../../gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[1]/tei:lg/tei:l' 

print smart_str(search_terms) + '\n'
print poem_nodes + '\n'

query = ' \
        declare variable $query := "%s" ; \
            declare variable $poem_nodes as node()* := %s; \
            declare variable $perpage := 3; \
            let $start := %s \
            let $end := %s \
            let $total := count($poem_nodes[matches(./string(), $query, "i")]) \
            for $x at $i in $poem_nodes[matches(./string(), $query, "i")] \
            return $x[$i = ($start to $end)] \
            ' % (smart_str(search_terms), poem_nodes, start, end)
            
print query + '\n'            

container = mgr.openContainer("../../gutorglyn.bdbxml")
qcontext = mgr.createQueryContext()
qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")
results = mgr.query(query,qcontext)

count = 1

mylines = {}

while results.hasNext():
    value = results.next()
    document = value.asDocument()
    name = document.getName()
    content = value.asString()
    print content
    count +=1

del container

print(datetime.now()-startTime)