import logging
import logging.config
import os
from os import path as Path
import time as Time

if os.getenv('SNTF_HOME'):
    logging.config.fileConfig(os.path.join(os.getenv('SNTF_HOME'), 'selfconf', 'logging.conf'))
else:
    sys.exit('SNTF_HOME is not set')
log = logging.getLogger('SNTF')

root_log_dir = 'logs'

def create_log_dir():
    time = Time.strftime('%Y-%m-%d-%H-%M-%S')
    logdir ='-'.join(['SNTF', time])
    logpath = Path.join(os.getenv('SNTF_HOME'), root_log_dir, logdir)
    if not Path.exists(logpath):
        os.makedirs(logpath)
    return logpath
