"""logging작성방법"""
import logging


logging.basicConfig(level=logging.DEBUG) # DEBUG부터 출력
# logging.basicConfig(level=logging.INFO) # INFO부터 출력

logging.critical('This is a critical message')
logging.error('This is an error message')
logging.warning('This is a warning message')
logging.info('This is an info message')
logging.debug('This is a debug message')


"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""