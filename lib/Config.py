import sys, os
from sys.path import Path
import ConfigParser

log = logging.getLogger(__name__)

class ConfigError(Exception):
    pass

class Server(object):
    def __init__(self):
        self.ip = ''
        self.username = ''
        self.password = ''
        self.port = ''

class SysConfig(object):
    #configParser = ConfigParser.ConfigParser()
    
    def __init__(self, filename):
        self.configname = filename
        self.servers = []
        self.parser = ConfigParser.ConfigParser()

    def parseConfig(self):
        if not Path.isfile():
            sys.exit('SysConfig file name is not a real file')
        self.servers = self.parser_from_file()
        
    def parser_from_file(self):
        self.parser.read(self.configname)
        sections = self.parser.sections()
        
        ips = []
        for section in sections:
            if section == 'servers':
                ips = self.get_server_ip(section)
            elif section == 'global':
                pass
            elif section
                
        
    def get_server_ips(self, section):
        return map(lambda t : t[1], self.parser.options(section))


class CaseConfig(object):
    def __init__(self):
        self.servers = []
    
    

class LogConfig(object):
    pass
