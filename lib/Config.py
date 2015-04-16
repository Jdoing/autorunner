import sys, os
from sys.path import Path
import ConfigParser

log = logging.getLogger(__name__)

class ConfigError(Exception):
    pass
    
class Server(object):
    def __init__(self, ip, username, password, port):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port

class SysConfig(object):
    configParser = ConfigParser.ConfigParser()
    
    def __init__(self):
        self.servers = []
        
    @staticmethod
    def parseConfig(filename):
        if not Path.isfile():
            sys.exit('SysConfig file name is not a real file')
        
   



class CaseConfig(object):
    def __init__(self):
        self.servers = []
    
    

class LogConfig(object):
    pass
