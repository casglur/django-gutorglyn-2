from __future__ import with_statement
from whoosh import index

indexdir = "c:/remove/whoosh/index"

ix = index.open_dir(indexdir)

with ix.searcher() as searcher:
    print list(searcher.lexicon("body"))    

