import unittest
import os, sys
import re

if os.getenv('SNTF_HOME'):
    sys.path.append(os.getenv('SNTF_HOME'))
    from lib.config import CaseConfig, SysConfig
else:
    sys.exit('SNTF_HOME is not set')

'''
class CaseConfigTest(unittest.TestCase):
    def test_parse_config(self):
        testcase = 'ExampleTest.Basic.ComputerTest.CalculatorTest.test_add'
        conf_path = r'/home/jiangyu/github/autorunner/caseconf/Basic.conf'
        conf = CaseConfig()
        conf.parse_config(conf_path)
        print conf
        #self.assertIn(conf.
'''
class SysConfigTest(unittest.TestCase):
    def test_parseConfig(self):
        conf = SysConfig()
        conf_path = r'/home/jiangyu/github/autorunner/sysconf/multiple.ini'
        conf.parse_from_config(conf_path)
        print str(conf.ini)
        #for i in conf.ini:
         #   print i, conf.ini[i]

if __name__ == '__main__':
    unittest.main()
