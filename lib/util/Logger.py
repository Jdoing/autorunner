import logging
import os
from os import path as Path
import time as Time

root_log_dir = 'logs'

def createLogDir():
    time = Time.strftime('%Y-%m-%d-%H-%M-%S')
    logdir ='-'.join(['autorunner', time])
    logpath = Path.join(os.getcwd(), root_log_dir, logdir)
    if not Path.exists(logpath):
        os.makedirs(logpath)
