
from bsddb3.db import *
from dbxml import *
from datetime import datetime
from django.utils.encoding import smart_str

startTime = datetime.now()

mgr = XmlManager()
# query = "collection('../../gutorglyn.bdbxml')//div[@xml:id='Guto001top']/div[@type='lev3']/lg/l[@n='1']"

search_terms = 'garw'
start = 0 
end = 40

poem_nodes = 'collection("../../gutorglyn.bdbxml")/tei:TEI/tei:text[1]/tei:body[1]/tei:div[1]/tei:div[1]/tei:div[1]/tei:lg/tei:l' 
poem_nodes1 = 'collection("../../gutorglyn.bdbxml")//tei:div[@type="lev0"]/tei:div/tei:lg/tei:l' 
 
query = ' \
            declare function functx:add-attributes \
              ( $elements as element()* , \
                $attrNames as xs:QName* , \
                $attrValues as xs:anyAtomicType* )  as element()? { \
                \
               for $element in $elements \
               return element { node-name($element)} \
                              { for $attrName at $seq in $attrNames \
                                return if ($element/@*[node-name(.) = $attrName]) \
                                       then () \
                                       else attribute {$attrName} \
                                                      {$attrValues[$seq]}, \
                                $element/@*, \
                                $element/node() } \
             } ; \
            declare variable $query := "%s"; \
            declare variable $poem_nodes as node()* := %s; \
            declare variable $perpage := 3; \
            let $start := %s \
            let $end := %s \
            let $total := count($poem_nodes[matches(., $query)]) \
            for $x at $i in $poem_nodes[matches(., $query, "i")] \
            return functx:add-attributes($x[$i = ($start to $end)], (xs:QName("position"),xs:QName("total")), ($i, $total + 1)) \
            ' % (smart_str(search_terms), poem_nodes, start, end)

container = mgr.openContainer("../../gutorglyn.bdbxml")
qcontext = mgr.createQueryContext()
qcontext.setNamespace("tei", "http://www.tei-c.org/ns/1.0")
qcontext.setNamespace("functx", "http://www.functx.com")
results = mgr.query(query,qcontext)

count = 1

mylines = []

while results.hasNext():
    count +=1
    
    value = results.next()
    document = value.asDocument()
    name = document.getName()
    content = value.asString()
    
#     parent = value.getParentNode()
#     while parent.hasNext():
#         parent_val = parent.next()
        
    
    mylines.append(content)
    
    attributes = value.getAttributes()
    while attributes.hasNext():
        attribute = attributes.next()
        attname = attribute.getNodeName()
        attvalue = attribute.getNodeValue()
        print attname + ' = ' + attvalue
        

print mylines

del container

print(datetime.now()-startTime)