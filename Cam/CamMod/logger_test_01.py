#coding=utf-8
# import logging
# # import logging.config
# #这个是配置文件的路径
# # CONF_LOG = "../Config/log.conf"
# # logging.config.fileConfig(CONF_LOG)
# logger = logging.getLogger()
# #下面就是使用日志打印日志信息
# logger.info("info类型的日志")
# logger.error("error 的日志")

'''
import logging
# logger=logging.basicConfig(level=logging.INFO,
#                     format='\n\r%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a,%d %b %Y %H:%M:%S',
#                     filename='logger_study01.log',
#                     filemode='a')
# # logger = logging.getLogger()
# #下面就是使用日志打印日志信息
logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s %(funcName)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filename='logger_study01.log',
                            filemode='a')
logger = logging.getLogger()
#
# logger.info("info类型的日志")
# logger.error("error 的日志")


def feibo(x):

    logging.info('an error occurred')
    if x == 1:
        return 0
    if x ==2:
        return 1
    else:
        return  feibo(x-1)+feibo(x-2)


# logger.info('fx start')
print(feibo(3))
'''

import logging
import os
l = logging.Logger('root')          #创建Logger对象
log = logging.getLogger('root')     #通过logging.getLogger创建Logger对象
print (l)                          #<logging.Logger object at 0x0000000001DF5B70>
print (log)                           #<logging.Logger object at 0x00000000022A16D8>


'''Handler'''
handler = logging.Handler()         #创建Handler对象
handler.__init__(logging.DEBUG)     #通过设置level来初始化Handler实例
handler.createLock()                #初始化一个线程锁可以用来序列化访问底层I / O功能,这可能不是线程安全的。
handler.acquire()                   #获取线程锁通过handler.createLock()
handler.release()                   #释放线程锁通过获取handler.acquire()
handler.setLevel(logging.DEBUG)     #设置临界值，如果Logging信息级别小于它则被忽视，当一个handler对象被创建，级别没有被设置，导致所有的信息会被处理。

handler.setFormatter("%(levelname)s,%(message)s")              #设置格式
# handler.addFilter(filter)         #添加指定的过滤器
# handler.removeFilter(filter)      #移除指定的过滤器
# handler.filter(record)            #通过设置过滤器适用于记录并返回真值如果要处理的记录
handler.flush()                     #确保所有的日志输出已经被刷新
handler.close()                     #收拾任何所使用资源处理程序,
# handler.handle(record)            #有条件地发出指定的日志记录,这取决于过滤器可能被添加到处理程序。
# handler.handlerError(record)      #处理错误
# handler.format(record)            #格式输出
# handler.emit(record)



























