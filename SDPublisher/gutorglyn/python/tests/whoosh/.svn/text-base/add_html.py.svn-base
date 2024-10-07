
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
from whoosh import index

indexdir = "c:/remove/whoosh/index"
html_doc = "<html><head><title>my web title</title></head><body>my web content</body></html>"

ix = index.open_dir(indexdir)
writer = ix.writer()
writer.add_document(title=u"Title 3", body=u"sixty sausages")
writer.commit()
