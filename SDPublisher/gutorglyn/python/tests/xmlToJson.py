# -*- coding: UTF-8 -*-
import untangle
import simplejson as json

print 'Starting to untangle...'
myurl = 'http://localhost/al/xml/patron-xml.xml'

mydict = {}

o = untangle.parse(myurl)
for patron in o.patrons.patron:
    nameid = patron.id['xml:id']
    name = patron.name.cdata   
    mydict['nameid'] = nameid
    mydict['name'] = name
    print mydict
    print json.dumps(mydict, indent=4) 
