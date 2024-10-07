import os, os.path
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
from whoosh import index

indexdir = "c:/remove/whoosh/index"

schema = Schema(body=TEXT(analyzer=StemmingAnalyzer()))

if not os.path.exists(indexdir):
    os.mkdir(indexdir)

ix = index.create_in(indexdir, schema)

