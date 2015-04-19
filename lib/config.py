import sys, os
from os import path as Path
import ConfigParser
import re
import logging
import json
from lib.exception import ConfigError

log = logging.getLogger(__name__)

__all__ = ['Case', 'CaseConfig']

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
    def __init__(self, name, time=0, errorType=None, errorMessage=None, status='pass', params={}):
        self.name = name
        self.time = time
        self.errorType = errorType
        self.errorMessage = errorMessage
        self.status = status
        self.params = params

class CaseConfig(object):
    def __init__(self):
        self.configname = ''
        self.cases = []
    
    def parse_config(self, filename):
        if not Path.exists(filename):
            sys.exit('case config not exists!')
        
        self.configname = filename
        self._get_case_conf()
    
    def _get_case_conf(self):
        with open(self.configname) as file:
            for line in file:
                line = line.strip()
                if line.startswith('#') or len(line) <= 0:
                    continue
                self._parse_line(line)
    
    def __str__(self):
        return str([('casename is: ' + case.name, 'params is: '+ str(case.params)) for case in self.cases])
            
    
    def _parse_line(self, line):
        splitline = line.split(',', 1)
        name = splitline[0]
        params = {}
        if len(splitline) > 1:
            try:
                param_string = splitline[1].split('=', 1)
                params = json.loads(param_string[1])
            except ConfigError, ex:
                print 'parse params occur error'
                raise ex
        self.update_cases(name = name, params = params)
            
    def update_cases(self, **kwargs):
        case = Case(kwargs['name'])
        case.name = kwargs['name']
        if kwargs['params']:
            case.params = kwargs['params'] 
        self.cases.append(case)

class LogConfig(object):
    pass
