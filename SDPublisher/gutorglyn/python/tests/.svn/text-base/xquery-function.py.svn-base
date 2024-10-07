# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *
from datetime import datetime
from django.utils.encoding import smart_str

# query = raw_input('Enter regular expression: ')
query = "Euraw"

startTime = datetime.now()

print 'Working on ' + '"%s"...' % query

mymgr = XmlManager()

myquery = 'declare function local:copyme($foo as xs:string) as xs:string { \
    let $bar := $foo \
        return $bar \
    }; \
    let $newval := local:copyme("pong") \
    return $newval'


mycontainer = mymgr.openContainer("../../gutorglyn.bdbxml")
qcontext = mymgr.createQueryContext()
qcontext.setDefaultCollection("../gutorglyn.bdbxml")
qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")

queryexp = mymgr.prepare(myquery, qcontext)

results = queryexp.execute(qcontext)

count = 0
          
for value in results:
    content = value.asString()
    count += 1
    print content
    
print 'Returns ' + str(count) + ' results for ' + '"%s"' % query

del mycontainer

print(datetime.now()-startTime)