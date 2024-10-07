
from bsddb3.db import *
from dbxml import *

try: 
    myenv = DBEnv()
    myenv.remove("/SDPublisher/SDPublisher/gutorglyn", DB_FORCE)
    print 'Environment removed!'
    DBEnv().close()

except XmlException, inst:
        print "XmlException (", inst.exceptionCode,"): ", inst.what
        if inst.exceptionCode == DATABASE_ERROR:
            print "Database error code:",inst.dbError

