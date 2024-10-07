# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *
from datetime import datetime
from django.utils.encoding import smart_str

# query = raw_input('Enter regular expression: ')
query = ".ddas"

startTime = datetime.now()

print 'Working on ' + '"%s"...' % query

mymgr = XmlManager()
# myquery = "for $line in " \
#     "collection('../../gutorglyn.bdbxml')//tei:div[@type='lev1']/tei:lg/tei:l " \
#     "where some $value " \
#     "in $line " \
#     "satisfies (matches($value, '%s', 'imx')) " \
#     "return $line" % (query)
#     uchel
myquery = "for $lines in collection('../../../gutorglyn.bdbxml')//tei:div[@type='lev1']/tei:lg/tei:l where some $line in $lines satisfies matches($line, '%s') return tokenize($lines, 'uchel')" % (smart_str(query))   

mycontainer = mymgr.openContainer("../../../gutorglyn.bdbxml")
qcontext = mymgr.createQueryContext()
qcontext.setDefaultCollection("../../gutorglyn.bdbxml")
qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")

queryexp = mymgr.prepare(myquery, qcontext)

results = queryexp.execute(qcontext)

count = 0
          
# for value in results:
#     document = value.asDocument()
#     name = document.getName()
#     content = value.asString()
#     count += 1
#     print name + " - " + content
#     
# print 'Returns ' + str(count) + ' results for ' + '"%s"' % query

for value in results:
    content = value.asString()
    print content

del mycontainer

print(datetime.now()-startTime)