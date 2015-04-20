from optparse import OptionParser
import sys
import logging

__all__ = ['ArgParser']

class ArgParser(object):
    def __init__(self):
        usage = '''usage: %prog [options]

        Examples:
        ./run.py -i tmp/local.ini -t performance.perf.DiskDrainRate
        ./run.py -i tmp/local.ini -t performance.perf.DiskDrainRate.test_9M
        '''
        self.parser = OptionParser(usage)
        self.options, self.args = None, None
    
    def addArgs(self):
        self.parser.add_option("-t", "--test", dest="casename", help="the filepath of casename", default = None)
        self.parser.add_option("-c", "--conf", dest="caseconf", help="the testcase of config", default = None)
        self.parser.add_option("-i", "--ini", dest="sysconf", help="the servers of config", default = None)

    
    def parse(self, argv):
        self.addArgs()
        (self.options, self.args) = self.parser.parse_args(argv)
        
        if not any((self.options.casename, self.options.caseconf)):
            self.parser.print_usage()
            sys.exit('error: you can not run without inputing casename or caseconf!')
    
