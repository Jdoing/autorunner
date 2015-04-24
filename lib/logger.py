import logging, logging.config
import os
import sys


log = None

def get_logger():
    global log
    if log:
        return log
    else:
        if os.getenv('SNTF_HOME'):
            logging.config.fileConfig(os.path.join(os.getenv('SNTF_HOME'), 'selfconf', 'logging.conf'))
            log = logging.getLogger('SNTF')
            return log
        else:
            print 'SNTF_HOME is not set'
            sys.exit(1)

'''
def get_logger():
    if get_logger.log:
        return get_logger.log
    else:
        if os.getenv('SNTF_HOME'):
            logging.config.fileConfig(os.path.join(os.getenv('SNTF_HOME'), 'selfconf', 'logging.conf'))
            get_logger.log = logging.getLogger('SNTF')
            return get_logger.log
        else:
            print 'SNTF_HOME is not set'
            sys.exit(1)
            
get_logger.log = None
'''
if __name__ == '__main__':
    log1 = get_logger()
    log1.debug('log1 id is %d' % id(log1))
    
    log2 = get_logger()
    log2.debug('log1 id is %d' % id(log2))
