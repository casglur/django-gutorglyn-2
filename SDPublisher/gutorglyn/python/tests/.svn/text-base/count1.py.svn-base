
from bsddb3.db import *
from dbxml import *
from datetime import datetime
from django.utils.encoding import smart_str

startTime = datetime.now()

mgr = XmlManager()

search_terms = '(^|[^a-z])ond([^a-z]|$)'

poem_nodes = 'collection("../../gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[1]/tei:lg/tei:l' 

query = ' \
            declare variable $query := "%s"; \
            declare variable $poem_nodes as node()* := %s; \
            let $total := count($poem_nodes[matches(., $query, "i")]) \
            return $total \
            ' % (smart_str(search_terms), poem_nodes)
             

container = mgr.openContainer("../../gutorglyn.bdbxml")
qcontext = mgr.createQueryContext()
qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")
results = mgr.query(query,qcontext)

mylines = {}

while results.hasNext():
    value = results.next()
    content = value.asString()
    print content + ' hits...'

del container

print(datetime.now()-startTime)