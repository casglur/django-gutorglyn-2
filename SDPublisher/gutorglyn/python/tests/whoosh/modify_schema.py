
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
from whoosh import index

indexdir = "c:/remove/whoosh/index"

ix = index.open_dir(indexdir)
ix.add_field("title", TEXT(stored=True))