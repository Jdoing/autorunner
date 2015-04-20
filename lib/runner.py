import sys, os
import unittest
import time
import os.path as Path
sys.path.append("..")
from xunit import XUnitTestResult
from util import logger
from config import *
#from util.parser import ArgParser
from TestInput import TestInputSingleton
from util.logger import log

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
            conf.parseConfig(self.argParser.options.sysconf)
            self._update_sys_conf(conf)
    
    def _update_sys_conf(self, conf):
        log.debug('_update_sys_conf ')
        TestInputSingleton.servers = conf.servers
    
    '''
    def executeByCaseName(self, casename):
        #case = Path.basename(casename)
        #self.suite = self.testLoader.loadTestsFromName(casename)
        self.getTestCaseByCaseName(casename)
        
        for case in self.tests:
            try:
                #load test case
                self.suite = self.testLoader.loadTestsFromName(case.name)
            except AttributeError:
                raise
            else:
                try:
                    #run test case
                    self._executeTest(self.suite)
                except Exception as ex:
                    case.status = 'fail'
                    case.errorType = 'AssertionError'
                    case.errorMessage = str(ex)

                finally:
                    #write report
                    if self.result.errors or self.result.failures:
                        case.status = 'fail'
                        case.errorType = 'AssertionError'
                        #print 'result  self.result.errors
                        case.errorMessage = self.result.failures[0][1]
                    self.writeReport(case)
    '''
    
    def writeReport(self, case):
        str_time = time.strftime("%y-%b-%d_%H-%M-%S", time.localtime())
        log_dir_path = logger.create_log_dir()
        self.report.add_test(**case.__dict__)
        self.report.write("{0}{2}report-{1}".format(log_dir_path, str_time, os.sep))
    
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
                    case.errorType = 'AssertionError'
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

        
    '''
    def _executeTest(self, suite):
        self.result = self.runner.run(suite)
    '''
    
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
        
    '''
    def executeByConf(self, confName):
        if not Path.isfile(confName):
            sys.exit("confName {0} was not found".format(confName))
        else:
            caseconf = CaseConfig()
            caseconf.parse_config(confName)
            
            TestInputSingleton.caseconf = caseconf
            
            casenames = [case.name for case in caseconf.cases]
            self.suite = self.testLoader.loadTestsFromNames(casenames)
            self._executeTest(self.suite)
    '''
            
    """
    def findTestMethodByClassName(self, classname):
        classPath = os.sep.join(classname.split('.')) + '.py'
        os.chdir(r'/home/jiangyu/github/autorunner')
        classPath = Path.join(os.getcwd(), classPath)
        print classPath
        print 
        if Path.isfile(classPath):
            print dir(classname)
        else:
            print "This is a method "
     """
