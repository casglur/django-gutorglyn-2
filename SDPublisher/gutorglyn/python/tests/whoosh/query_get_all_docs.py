from __future__ import with_statement
from whoosh import index
from whoosh.fields import Schema
from whoosh.qparser import QueryParser

indexdir = "c:/remove/whoosh/index"
ix = index.open_dir(indexdir)
searcher = ix.searcher()
for stored_fields in searcher.documents():
    print(stored_fields['body'])