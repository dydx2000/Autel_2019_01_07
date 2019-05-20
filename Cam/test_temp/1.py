import traceback
try:
    10/0
except:
    f=open("tracelog.txt",'a')
    traceback.print_exc(file=f)
    f.flush()
    f.close()


#  logging.exception('------------Exceptions Caught--------')
#
# logging.exception(ParaError)