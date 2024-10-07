from whoosh import index

indexdir = "c:/remove/whoosh/index"

ix = index.open_dir(indexdir)

try:
    searcher = ix.searcher()
    print list(searcher.lexicon("body"))    
finally:
    searcher.close()
