# -*- coding: UTF-8 -*-
from bsddb3.db import *
from dbxml import *

manager = XmlManager()
container = manager.openContainer("../gutorglyn.bdbxml")

document = container.getDocument("guto001.xml")
value = XmlValue("guto001.xml")
document.setMetaData("http://www.tei-c.org/ns/1.0", "tei", value)
container.updateDocument(document, manager.createUpdateContext())

del container
