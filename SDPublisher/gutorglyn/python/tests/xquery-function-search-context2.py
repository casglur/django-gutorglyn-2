# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *
from datetime import datetime
from django.utils.encoding import smart_str

userdoc = "collection('../../gutorglyn.bdbxml')/tei:TEI/tei:text/tei:body/tei:div/tei:div/tei:div/tei:lg"

# query = raw_input('Enter regular expression: ')
query = "Euraw"


startTime = datetime.now()

print 'Working on ' + '"%s"...' % query

mymgr = XmlManager()
# myquery = " \
#         declare function local:match-lines-num($doc as node()*, $term as xs:string) as xs:integer* { \
#             for $lines in $doc \
#             where some $line\
#             in $lines \
#             satisfies (matches($lines, $term, 'im')) \
#             return functx:index-of-deep-equal-node($doc, $lines) \
#         }; \
#         for $line-groups in collection('../../gutorglyn.bdbxml')/tei:TEI/tei:text/tei:body/tei:div/tei:div/tei:div/tei:lg  \
#         where some $line-group  \
#         in $line-groups  \
#         satisfies (matches($line-group, '%s', 'im'))  \
#         return $line-groups" % (functx_prefix, query)


myquery = ' \
        declare variable $query := "Euraw";\
        declare variable $user_doc as node()* := %s; \
         \
        declare function local:remove-elements($input as element()*) as element() {  \
           element {node-name($input) } \
              {$input/@*, \
              attribute title {$input/preceding-sibling::element(head)}, \
              attribute xml:id {$input/../@xml:id}, \
               for $child in $input/node() \
                  return \
                     if ($child[matches((.),$query)] instance of element()) \
                        then ( \
                        $child/preceding-sibling::*[2], \
                        $child/preceding-sibling::*[1], \
                        $child, \
                        $child/following-sibling::*[1], \
                        $child/following-sibling::*[2] \
                        ) \
                        else () \
              } \
        }; \
         \
        for $i in (1 to count($user_doc)) \
        return ( \
            if (matches($user_doc[$i], $query)) \
            then \
            (local:remove-elements($user_doc[$i])) \
            else () \
            )' % userdoc


mycontainer = mymgr.openContainer("../../gutorglyn.bdbxml")
qcontext = mymgr.createQueryContext()
qcontext.setDefaultCollection("../gutorglyn.bdbxml")
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