#!/usr/bin/python
import unittest
import os, sys


class RunnerTest(unittest.TestCase):
    def setUp(self):
        os.chdir(r'/home/jiangyu/github/autorunner')
        print os.getcwd()
        from lib.TestRunner.Runner import Runner
    
    def test_findTestMethod(self):
        runner = Runner()
        runner.findTestMethod('ExampleTest.Basic.ComputerTest')

if __name__ == '__main__':
    unittest.main(verbosity = 2)
