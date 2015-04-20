#!/usr/bin/python
#coding=utf-8
import sys, os
sys.path = ["lib", "testcase"] + sys.path
import logging
import logging.config
import signal
if sys.hexversion < 0x02060000:
    print "Testrunner requires version 2.6+ of python"
    sys.exit()
from util.logger import log
#from util.parser import ArgParser
from optparse import OptionParser
from runner import Runner
from xunit import XUnitTestResult

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

def main():
    #parse command line args
    argParser = ArgParser()
    argParser.parse(sys.argv)

    try:
        runner = Runner(argParser)
        #print dir(argParser)
        
        runner.run()
        
        '''
        if argParser.options.casename:
            casename = argParser.options.casename
            runner.executeByCaseName(casename)
        if argParser.options.confname:
            runner.executeByConf(argParser.options.confname)
        '''
    except Exception, e:
        log.error('run error: %s' % e)

if __name__ == '__main__':
    child = os.fork()
    if child == 0:
        main()
    else:
        try:
            os.wait()
        except KeyboardInterrupt:
            print 'KeyBoardInterrupt'
            try:
                os.kill(child, signal.SIGKILL)
            except OSError:
                pass
        except OSError:
                pass
    sys.exit()

