#!/usr/bin/python
#coding=utf-8
import sys, os
sys.path = ["lib", "testcase"] + sys.path
import logging
import logging.config
import signal
import unittest
import time
import os.path as Path
from optparse import OptionParser

if sys.hexversion < 0x02070000:
    print "Testrunner requires version 2.7+ of python"
    sys.exit()
#from util.logger import log

from xunit import XUnitTestResult
from config import Case, SysConfig, CaseConfig
from TestInput import TestInputSingleton
import logger

if os.getenv('SNTF_HOME'):
    print 'root_dir is: %s' % os.getenv('SNTF_HOME')
else:
    sys.exit('SNTF_HOME is not set')

log = logger.get_logger()

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



class Runner(object):
    def __init__(self, argParser, verbose = 2):
        self.suite = None
        self.testLoader = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity = verbose)
        self.tests = []
        self.report = XUnitTestResult()
        self.result = None
        self.argParser = argParser
        
    def run(self):
        self._get_testcase()
        self._get_sys_conf()        
        self._run_case()   
    
    def _get_sys_conf(self):
        if self.argParser.options.sysconf:
            log.debug('sys conf is: %s' % self.argParser.options.sysconf)
            conf = SysConfig()
            conf.parse_from_config(self.argParser.options.sysconf)
            self._update_ini_conf(conf)
    
    def _update_ini_conf(self, conf):
        log.debug('_update_ini_conf ')
        TestInputSingleton.ini_config = conf.ini

    def writeReport(self, case):
        str_time = time.strftime("%y-%b-%d_%H-%M-%S", time.localtime())
        log_dir_path = self._create_log_dir()
        self.report.add_test(**case.__dict__)
        self.report.write("{0}{2}report-{1}".format(log_dir_path, str_time, os.sep))
        
    def _create_log_dir(self):
        str_time = time.strftime('%Y-%m-%d-%H-%M-%S')
        logdir ='-'.join(['SNTF', str_time])
        logpath = Path.join(os.getenv('SNTF_HOME'), 'logs', logdir)
        if not Path.exists(logpath):
            os.makedirs(logpath)
        return logpath
    
    def _run_case(self):
        for case in self.tests:
            # Update the test params for each test
            self._update_test_params(case = case)  
            try:
                #load test case
                self.suite = self.testLoader.loadTestsFromName(case.name)
            except AttributeError, e:
                print "Test {0} was not found: {1}".format(case.name, e)
            except SyntaxError, e:
                print "SyntaxError in {0}: {1}".format(case.name, e)
            else:
                try:
                    self.result = self.runner.run(self.suite)
                except Exception, ex:
                    case.status = 'fail'
                    case.errorType = type(ex).__name__
                    case.errorMessage = str(ex)
                finally:
                    #write report
                    if self.result.errors or self.result.failures:
                        case.status = 'fail'
                        case.errorType = 'AssertionError'
                        #print 'result  self.result.errors
                        case.errorMessage = self.result.failures[0][1]
                    self.writeReport(case)

    def _update_test_params(self, **kwargs):
        TestInputSingleton.test_params = kwargs['case'].params
    
    def _get_testcase(self):
        caseconf = None
        if self.argParser.options.casename:
            self.getTestCaseByCaseName(self.argParser.options.casename)
        if self.argParser.options.caseconf:
            caseconf = self.getTestCaseByConf(self.argParser.options.caseconf)
        return caseconf
            
    def getTestCaseByConf(self, configname):
        if not Path.isfile(configname):
            sys.exit("confName {0} was not found".format(configname))
        else:
            caseconf = CaseConfig()
            caseconf.parse_config(configname)
            self.tests.extend(caseconf.cases)
            return caseconf
    
    def getTestCaseByCaseName(self, name):
        if name.find('*') > 0:
            prefix = ".".join(name.split(".")[0:-1])
            for t in unittest.TestLoader().loadTestsFromName(name.rstrip('.*')):
                #new a case object
                case = Case(prefix + '.' + t._testMethodName)
                self.tests.append(case)
        else:
            case = Case(name)
            self.tests.append(case)
            
    def getTestCaseByDir(self, dir_path):
        if not os.path.isdir(dir_path):
            print '[%s] is not dir' % dir_path
            sys.exit(1)
        
        for dirname, subdirs, files in os.walk(dir_path):
            for test_file in files:
                if re.match('^.*\.py$', test_file):
                    file_name = os.path.join(dirname, test_file)
                    self.tests.extend(self.getTestCaseByFile(file_name))
                    
                    
    
    def getTestCaseByFile(self, file_name):
        
        module_name = test_file[:test_file.rfind('.')]
        
        

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

