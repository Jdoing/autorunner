#!/usr/bnin/python
import sys, os
import unittest
sys.path.append(r'/home/jiangyu/github/autorunner/Example')
from Computer import Calculator
'''
if os.getenv('SNTF_HOME'):
    sys.path.append(os.path.join(os.getenv('SNTF_HOME'), 'Example'))
    sys.path.append(os.path.join(os.getenv('SNTF_HOME'), 'lib'))
    #import Example, lib.TestInput.TestInputSingleton
    from Computer import Calculator
    from TestInput import TestInputSingleton

else:
    print 'SNTF_HOME env is not set'
    sys.exit('SNTF_HOME env is not set')
'''

x = 10

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.cal = Calculator()
    
    def test_add(self):
        
        self.assertEqual(self.cal.add(2, 3), 5, 'test add func')
    
    def test_sub(self):
        self.assertEqual(self.cal.sub(5, 2), 3, 'test sub func')
    
    def test_mul(self):
        self.assertEqual(self.cal.mul(1, 3), 3, 'test mul func')

    def test_div(self):
        self.assertEqual(self.cal.div(6, 2), 3, 'test div func')

if __name__ == '__main__':
    unittest.main(verbosity = 2)
