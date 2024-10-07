from __future__ import with_statement
from whoosh import index
from whoosh.fields import Schema
from whoosh.qparser import QueryParser

indexdir = "c:/remove/whoosh/index"

ix = index.open_dir(indexdir)

qp = QueryParser("body", schema=ix.schema)
q = qp.parse(u"sixty")

with ix.searcher() as s:
    results = s.search(q)
    for result in results:
        docs = result
        print docs
