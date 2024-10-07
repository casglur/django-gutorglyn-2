# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *
from datetime import datetime
from django.utils.encoding import smart_str
from django.utils.http import urlquote

query = raw_input('Enter search term: ')

containsTypeChoice = raw_input('Enter 1 for case-sensitive or 2 for non case-sensitive: ')
diacriticsChoice = raw_input('Enter 1 for diacritic-sensitive or 2 for non diacritic-sensitive: ')


containsType = ''

if containsTypeChoice == '1':
    containsType = 'contains'
else:
    containsType = 'dbxml:contains'

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
myquery =   "for $lines in collection('../../../gutorglyn.bdbxml')//tei:div[@type='lev1']/tei:lg/tei:l \
            where some $line in $lines \
            satisfies %s($line, '%s') \
            return $lines" % (containsType, (query))    

mycontainer = mymgr.openContainer("../../../gutorglyn.bdbxml")
qcontext = mymgr.createQueryContext()
qcontext.setDefaultCollection("../../gutorglyn.bdbxml")
qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")

queryexp = mymgr.prepare(myquery, qcontext)

results = queryexp.execute(qcontext)

count = 0
          
for value in results:
    document = value.asDocument()
    name = document.getName()
    content = value.asString()
    count += 1
    print name + " - " + content
    
print 'Returns ' + str(count) + ' results for ' + '"%s"' % query

del mycontainer

print(datetime.now()-startTime)