import sys, os
from os import path as Path
import ConfigParser
import re
import logging
import json
#from lib.exception import ConfigError
#from util.logger import log
from run import log

__all__ = ['Case', 'SysConfig', 'CaseConfig']
'''
class Server(object):
    def __init__(self):
        self.ip = ''
        self.username = ''
        self.password = ''
        self.port = ''
'''
class SysConfig(object):
    def __init__(self):
        self.configname = ''
        #self.servers = []
        self.ini = {}

    def parse_from_config(self, filename):
        self.configname = filename
        self.ini = self._parse_from_config(filename)
    
    def _parse_from_config(self, filename):
        if not os.path.isfile(filename):
            log.err('SysConfig file name is not a real file')
            sys.exit(1)
        try:
            configParser = ConfigParser.ConfigParser()
            configParser.read(filename)
            conf = {}
            for section in configParser.sections():
                #match IP, section is ip, item is node information
                if re.match('^(\d{1,3}\.){3}?(\d{1,3})?$', section):
                    conf[section] = self._get_node_conf(configParser, section)
                else:
                    conf[section] = dict(configParser.items(section))
        except Exception, ex:
            sys.exit(ex)
        finally:
            return conf
            
    def _get_node_conf(self, configParser, section):
        nodeconf = 'subconf'
        node = dict([item for item in configParser.items(section) if item[0] != nodeconf])
        try:
            node[nodeconf] = self._parse_from_config(configParser.get(section, nodeconf))
        except:
            pass
        return node



    '''
    def __str__(self):
        for key, value in self.ini:
            print 'section is: '
            for k, v in value:
                if not isinstance(v, dict):
                    print 'key is %s, value is %s' % k, v
                else:
                    pass
    '''
    '''
    def _parser_from_file(self):
        configParser.read(self.configname)
        sections = configParser.sections()
        
        ips = []
        for section in sections:
            if section == 'servers':
                ips = self._get_server_ips(section)
            elif section == 'global':
                pass
            #match IP, section is ip, item is server information
            elif re.match('^(\d{1,3}\.){3}?(\d{1,3})?$', section):
                self._update_server(**dict(configParser.items(section), ip = section))
            else:
                pass
    '''
    
    '''
    def _update_server(self, **kwargs):
        server = Server()
        server.ip = kwargs['ip']
        server.username = kwargs['username']
        server.password = kwargs['password']
        server.port = kwargs['port']
        self.servers.append(server)
    '''
    '''
    def _get_server_ips(self, section):
        #return map(lambda t : t[1], configParser.items(section))
        return [item[1] for item in configParser.items(section)]
    '''
    
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
        if not os.path.exists(filename):
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
            except Exception, ex:
                print 'parse params occur error'
                raise ex
        self.update_cases(name = name, params = params)
            
    def update_cases(self, **kwargs):
        case = Case(kwargs['name'])
        if kwargs['params']:
            case.params = kwargs['params'] 
        self.cases.append(case)
