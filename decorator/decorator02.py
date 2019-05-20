import time
import datetime

'''
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')


@Foo
def bar():
    print('bar')


bar()
'''



from datetime import datetime


# Create your tests here.
class params:
    def __init__(self):
        print("init called")

    @staticmethod
    def released():
        print("release this class")


def pre_date(cls):
    def date(func):
        def wrapper():
            print("before %s ,we called (%s)." % (func.__name__, cls))
            try:
                func()
                date = datetime.utcnow()
                print(date)
            finally:
                cls.released()

        return wrapper

    return date


@pre_date(params)
def alan():
    print('alan speaking')


@pre_date(params)
def tom():
    print('tom speaking')


alan()
print()
tom()

#类装饰器
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self,x):
        print('class decorator runing')
        self._func(x)
        print('class decorator ending')


@Foo
def bar(x):
    print(x,'bar bar bar bar bar bar!!!')


bar(5)

