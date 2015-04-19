import unittest
import os, sys
import re

if os.getenv('SNTF_HOME'):
    sys.path.append(os.getenv('SNTF_HOME'))
    from lib.config import CaseConfig
else:
    sys.exit('SNTF_HOME is not set')


class CaseConfigTest(unittest.TestCase):
    def test_parse_config(self):
        testcase = 'ExampleTest.Basic.ComputerTest.CalculatorTest.test_add'
        conf_path = r'/home/jiangyu/github/autorunner/caseconf/Basic.conf'
        conf = CaseConfig()
        conf.parse_config(conf_path)
        print conf
        #self.assertIn(conf.
        
if __name__ == '__main__':
    unittest.main()
