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
from util import Logger
from util.Parser import ArgParser
from TestRunner.Runner import Runner
from xunit import XUnitTestResult

logging.config.fileConfig(os.path.join(os.getcwd(), 'selfconf', 'logging.conf'))
log = logging.getLogger('SNTF')

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
            #print runner.result
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

