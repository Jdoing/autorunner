import sys, os
import unittest
import time
import os.path as Path
sys.path.append("..")
from xunit import XUnitTestResult
from util import Logger

class Case(object):
    def __init__(self, name, time=0, errorType=None, errorMessage=None, status='pass', params=''):
        self.name = name
        self.time = time
        self.errorType = errorType
        self.errorMessage = errorMessage
        self.status = status
        self.params = params


class Runner(object):
    def __init__(self, verbose = 2):
        self.suite = None
        self.testLoader = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity = verbose)
        self.tests = []
        self.result = XUnitTestResult()
        self._result = None
        
        
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
                    if self._result.errors or self._result.failures:
                        case.status = 'fail'
                        case.errorType = 'AssertionError'
                        #print 'result  self._result.errors
                        case.errorMessage = self._result.failures[0][1]
                    self.writeReport(case)

    def writeReport(self, case):
        str_time = time.strftime("%y-%b-%d_%H-%M-%S", time.localtime())
        log_dir_path = Logger.create_log_dir()
        self.result.add_test(**case.__dict__)
        self.result.write("{0}{2}report-{1}".format(log_dir_path, str_time, os.sep))
        
    
    def executeByConf(self, confName):
        if not Path.isfile(confName):
            sys.exit("confName {0} was not found".format(confName))
        else:
            casenames = []
            confile = open(confName)
            for case in confile.readlines():
                _case = case.strip()
                casenames.append(_case)
            self.suite = self.testLoader.loadTestsFromNames(casenames)
            self._executeTest(self.suite)

    def _executeTest(self, suite):
        self._result = self.runner.run(suite)

    
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
