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
from util import logger
from util.parser import ArgParser
from testrunner.runner import Runner
from xunit import XUnitTestResult

def main():
    #parse command line args
    argParser = ArgParser()
    argParser.parse(sys.argv)

    try:
        runner = Runner()
        #print dir(argParser)
        if argParser.options.casename:
            casename = argParser.options.casename
            runner.executeByCaseName(casename)
        if argParser.options.confname:
            runner.executeByConf(argParser.options.confname)
        
    except Exception, e:
        print('run error: %s' % e)



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

