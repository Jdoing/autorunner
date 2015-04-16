import sys, os
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
    def __init__(self):
        self.servers = []
        
    @staticmethod
    def parseConfig(filename):
        
   



class CaseConfig(object):
    def __init__(self):
        self.servers = []
    
    

class LogConfig(object):
    pass
