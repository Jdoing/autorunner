import logging
import os
from os import path as Path
import time as Time

logging.config.fileConfig(os.path.join(os.getcwd(), 'selfconf', 'logging.conf'))
log = logging.getLogger('SNTF')

root_log_dir = 'logs'

def create_log_dir():
    time = Time.strftime('%Y-%m-%d-%H-%M-%S')
    logdir ='-'.join(['SNTF', time])
    logpath = Path.join(os.getcwd(), root_log_dir, logdir)
    if not Path.exists(logpath):
        os.makedirs(logpath)
    return logpath
