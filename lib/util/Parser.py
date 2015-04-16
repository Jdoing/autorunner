from optparse import OptionParser
import sys
import logging

log = logging.getLogger(__name__)

__all__ = ['ArgParser']

class ArgParser(object):
    def __init__(self):
        usage = "usage: %prog [options] arg"
        self.parser = OptionParser(usage)
        self.options, self.args = None, None
    
    def addArgs(self):
        self.parser.add_option("-t", "--test", dest="casename", help="the filepath of casename", default = None)
        self.parser.add_option("-c", "--conf", dest="confname", help="the testcase of config", default = None)
    
    
    def parse(self, argv):
        self.addArgs()
        (self.options, self.args) = self.parser.parse_args(argv)


class ConfParser(object):
    def parseConf(self, filename):
        f = open(filename, 'r')
        return f.readlines()
        
