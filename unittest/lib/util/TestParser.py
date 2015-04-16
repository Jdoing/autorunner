#!/usr/bin/python
import unittest
import sys, os
sys.path.append(r'/home/jiangyu/github/autorunner/lib')
from util.Parser import ArgParser

class TestArgsParser(unittest.TestCase):
    def testPaserWithCaseName(self):
        inputArgs = ['run.py', '-t', 'basictest']
        parser = ArgParser()
        parser.parse(inputArgs)
        self.assertEqual('basictest', parser.options.casename)



if __name__ == '__main__':
    unittest.main(verbosity = 2)
