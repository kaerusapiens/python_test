"""logging작성방법

CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging


# logging.basicConfig(level=logging.DEBUG) # DEBUG부터 출력
# # logging.basicConfig(level=logging.INFO) # INFO부터 출력

# logging.critical('This is a critical message')
# logging.error('This is an error message')
# logging.warning('This is a warning message')
# logging.info('This is an info message')
# logging.debug('This is a debug message')



FORMATTER = "%(asctime)s:%(levelname)s:%(message)s"
logging.basicConfig(level=logging.INFO, format=FORMATTER)
logging.info('%s', 'error_message')
#2025-02-24 22:54:07,011:INFO:error_message


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('%s', 'error_message')