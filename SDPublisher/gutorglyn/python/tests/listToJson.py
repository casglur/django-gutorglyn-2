
import simplejson as json
from bsddb3.db import *
from dbxml import *

mymgr = XmlManager()
myquery = "collection('../../gutorglyn.bdbxml')//tei:div[@type='nodyn_noddwr']/tei:div[@type='eng']/tei:head/descendant-or-self::text()"

mycontainer = mymgr.openContainer("../../gutorglyn.bdbxml")
qcontext = mymgr.createQueryContext()
qcontext.setDefaultCollection("../../gutorglyn.bdbxml")
qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")

queryexp = mymgr.prepare(myquery, qcontext)

results = queryexp.execute(qcontext)

data = []
          
for value in results:
    document = value.asDocument()
    name = document.getName()
    content = value.asString()
    data.append(content)
    
print 'DATA:', repr(data)

data_string = json.dumps(data)
print 'JSON:', data_string    

del mycontainer

