
from bsddb3.db import *
from dbxml import *

mgr = XmlManager()
# query = "collection('../../gutorglyn.bdbxml')//div[@xml:id='Guto001top']/div[@type='lev3']/lg/l[@n='1']"
query = "collection('../../gutorglyn.bdbxml')//tei:TEI"

container = mgr.openContainer("../../gutorglyn.bdbxml")
qcontext = mgr.createQueryContext()
qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")
results = mgr.query(query,qcontext)

count = 1

mylines = {}

while results.hasNext():
    value = results.next()
    content = value.asString()
    mylines[count] = content
    print type(value)
    count +=1

del container