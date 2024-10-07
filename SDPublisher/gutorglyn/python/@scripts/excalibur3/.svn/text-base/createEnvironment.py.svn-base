
from bsddb3.db import *
from dbxml import *

myenv = DBEnv()
myenv.set_cachesize(0, 10000000, 1)
myenv.open("C:/Users/lsrobert/Documents/shared work/external work/gutorGlyn/SDPublisher/gutorglyn", DB_CREATE|DB_INIT_LOCK|DB_INIT_LOG|DB_INIT_MPOOL|DB_INIT_TXN |DB_RECOVER, 0)
myenv.close(0)

print 'Success!'