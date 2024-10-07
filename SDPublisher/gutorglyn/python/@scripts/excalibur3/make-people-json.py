import libxml2
import libxslt

styledoc = libxml2.parseFile("../../static/xsl/xml-to-json.xsl")
style = libxslt.parseStylesheetDoc(styledoc)
doc = libxml2.parseFile("http://localhost:8000/gutorglyn/patron-xml")
result = style.applyStylesheet(doc, None)
style.saveResultToFilename("../../static/json/people.json", result, 0)
style.freeStylesheet()
doc.freeDoc()
result.freeDoc()