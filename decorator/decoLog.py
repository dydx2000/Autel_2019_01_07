#! /usr/bin/env python2.7


import logging

logging.basicConfig(format='[%(asctime)s] %(message)s', level=logging.INFO)


def time_recorder(func):
    """装饰器, 用在func方法执行前后, 增加运行信息"""

    def wrapper(*arg, **kw):
        logging.info("Begin to execute function: %s" % func.__name__)
        func(*arg, **kw)
        logging.info("Finish executing function: %s" % func.__name__)

    return wrapper


def time_recorder2(func):
    """装饰器, 用在func方法执行前后, 增加运行信息"""

    def wrapper():
        logging.info("recoder1 Begin to execute function: %s" % func.__name__)
        func()
        logging.info("recorder1 Finish executing function: %s" % func.__name__)

    return wrapper


@time_recorder
def first_func():
    print("I'm first_function. I'm doing something...")


@time_recorder2
def second_func():
    print("I'm second_function. I'm doing something...")


if __name__ == "__main__":
    first_func()
    # second_func()
