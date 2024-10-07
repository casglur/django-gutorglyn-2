# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *

mymgr = XmlManager()
myquery = "<select id='poem' name='poem'><option value='#'>Choose...</option> "
myquery = myquery + "{for $v in collection('../../../gutorglyn.bdbxml')//tei:div[@type='lev2'][2] "
myquery = myquery + "let $w := substring-after($v/@xml:id, 'Guto') "
myquery = myquery + "let $x := substring-before($w, 'translation') "
myquery = myquery + "let $y := $v/tei:lg[1]/tei:l[1]/descendant-or-self::text()"
myquery = myquery + "order by $v/@xml:id "
myquery = myquery + "return"
myquery = myquery + "<option value='{$x}'>"
myquery = myquery + "{$y}"
myquery = myquery + "</option>"
myquery = myquery + "}</select>"

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
    
    #content = content.replace("Guto","")
    content = content.replace("top","")
    
    print content

del mycontainer
