# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *

myStr = 'Aeth hawlwyr gynt i’th ddilyn,'
declareNamespace = 'declare namespace tei="http://www.tei-c.org/ns/1.0";'
searchFunction = 'contains($line, "%s")' % myStr
#searchFunction = '(dbxml:contains($line, "%s"))' % myStr
mymgr = XmlManager()
#myquery = r'%s for $lines in collection("../gutorglyn.bdbxml")//tei:div[@type="lev1"]/tei:lg/tei:l where some $line in $lines satisfies %s return $lines' % (declareNamespace, searchFunction)
#myquery = 'declare namespace tei="http://www.tei-c.org/ns/1.0"; count(collection("../gutorglyn.bdbxml")//tei:div[@type="lev1"]/tei:lg[contains(., "%s")])' % myStr

myquery = declareNamespace + 'collection("../gutorglyn.bdbxml")//tei:div[@type="lev1"]/tei:lg/tei:l[contains(., "%s")]/following-sibling::text()' % myStr

print myquery

mycontainer = mymgr.openContainer("../gutorglyn.bdbxml")
qcontext = mymgr.createQueryContext()
qcontext.setDefaultCollection("../gutorglyn.bdbxml")
queryexp = mymgr.prepare(myquery, qcontext)
queryResults = queryexp.execute(qcontext)

for value in queryResults:
    content = value.asString()
    print content

del mycontainer
