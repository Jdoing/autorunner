import sys, os
import unittest
import os.path as Path
sys.path.append(Path.join(os.getcwd(), 'lib'))

from xunit import XUnitTestResult

class Runner(object):
    def __init__(self, verbose = 2):
        self.suite = None
        self.testLoader = unittest.TestLoader()
        self.runner = unittest.TextTestRunner(verbosity = verbose)
        self.result = XUnitTestResult()
        
    def executeByCaseName(self, casename):
        #case = Path.basename(casename)
        self.suite = self.testLoader.loadTestsFromName(casename)
        
        
        
        self._executeTest(self.suite)
    
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
        self.result = self.runner.run(suite)
    
    
    def findTestMethod(self, classname):
        cwd = os.getcwd()
        classPath = classname.split('.').join(os.sep)
        if Path.join(cwd, 
