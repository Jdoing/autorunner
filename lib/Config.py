import sys, os
from sys.path import Path
import ConfigParser
import re
import logging

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
    
    def __init__(self):
        self.configname = ''
        self.servers = []
        self.parser = ConfigParser.ConfigParser()

    def parseConfig(self, filename):
        self.configname = filename
        if not Path.isfile():
            sys.exit('SysConfig file name is not a real file')
        self.servers = self._parser_from_file()
        
    def _parser_from_file(self):
        self.parser.read(self.configname)
        sections = self.parser.sections()
        
        ips = []
        for section in sections:
            if section == 'servers':
                ips = self.get_server_ip(section)
            elif section == 'global':
                pass
            elif re.match('^(\d{1,3}\.){3}?(\d{1,3})?$', section):
                self.servers[section] = dict(self.parser.items(section))
            else:
                pass

        
    def _get_server_ips(self, section):
        return map(lambda t : t[1], self.parser.items(section))

class Case(object):
    def __init__(self):
        self.casename = ''
        self.params = {}

class CaseConfig(object):
    def __init__(self):
        self.configname = ''
        self.cases = []
    
    def parseConfig(self, filename):
        if not Path.exists(filename):
            sys.exit('case config not exists!')
        
        self.configname = filename
        self.get_case_conf()
    
    def get_case_conf(self):
        file = open(filename)
        for line in f:
            line = line.strip()
            
        

class LogConfig(object):
    pass
