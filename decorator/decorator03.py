from time import time,sleep
import functools
def timer(func):
    @functools.wraps(func)
    def warpper(*args,**kw):
        tic=time()
        result=func(*args,**kw)
        toc=time()
        print (func.__name__)
        print ("%f seconds has passed"%(toc-tic))
        return result
    return warpper

@timer
def myfun():
    sleep(2)
    return "end"

myfun()
print (myfun.__name__ ) #wrapper
