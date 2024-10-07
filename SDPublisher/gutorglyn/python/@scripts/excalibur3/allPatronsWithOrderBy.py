# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *

mymgr = XmlManager()

myquery = "<patrons>{for $x in collection('../../../gutorglyn.bdbxml')//tei:div[@type='nodyn_noddwr'] order by $x/tei:div[@type='cym']/tei:head return <patron><id>{$x/@xml:id}</id><name>{$x/tei:div/tei:head/descendant-or-self::text()}</name></patron>}</patrons>"

mycontainer = mymgr.openContainer("../../../gutorglyn.bdbxml")
qcontext = mymgr.createQueryContext()
qcontext.setDefaultCollection("../../../gutorglyn.bdbxml")
qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")

queryexp = mymgr.prepare(myquery, qcontext)

results = queryexp.execute(qcontext)

for value in results:
    document = value.asDocument()
    name = document.getName()
    content = value.asString()
    content = content.replace(u"\u2019","'")
    content = content.replace(u"\u00F4","&ocirc;")
    content = content.replace(u"\u00E2","&acirc;")
    content = content.replace(u"\u00EF","&iuml;")
    content = content.replace(u"\u00E1","&aacute;")
    content = content.replace(u"\u0175","&wcirc;")    
    content = content.replace(u"\u0177","&ycirc;")
    content = content.replace(u"\u2013","&ndash;")
    content = content.replace(u"\u00EA","&ecirc;")
    content = content.replace(u"\u00FB","&ucirc;")
    
    print content

del mycontainer
