
import logging
# try:
#     1/0
# except Exception as e:
#     logging.exception("message")
#     # pass
# #
# try:
#     1 / 0
# except Exception, e:
#     logging.error(e)

import logging
# LOG_FILENAME = 'alog.txt'
logging.basicConfig(filename='alog.txt' )
#level=logging.DEBUG)

# logging.debug('This message should go to the log file')

try:
    1/0
except:
    logging.exception('-------------------Exceptions Caught---------------------------------')

