#-*- coding:utf-8 -*-
#只能选择输出到屏幕或文件
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a,%d %b %Y %H:%M:%S',
                    filename='test_01.log',
                    filemode='a')
'''
参数：
level：指定输出的日志级别
format：指定日志格式，包括：
    asctime：时间
    filename：日志归属的文件名称
    lineno：日志对应代码在归属文件中的行号
    levelname：日至最低级别，不指定默认为warning
    message：具体的日志内容，
datefmt：指定具体的时间格式，如果不指定，asctime将使用默认格式，如：2018-05-05 22:07:30,578 
filename：指定日志文件名称，可携带具体路径，不指定该参数时日志输出到屏幕
filemode：指定日志写入模式，默认为'a'表示追加，可以指定为'w'表示覆盖
'''
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

try:
    1/0
except:
    logging.exception('--------------Exceptions Caught--------')