#!/usr/bin/python
import os, sys
from lib import GlobalSet
#from lib.TestRunner.Runner import Runner

class Case(object):
    def __init__(self, name, time=0, errorType=None, errorMessage=None, status='pass', params=''):
        self.name = name
        self.time = time
        self.errorType = errorType
        self.errorMessage = errorMessage
        self.status = status
        self.params = params

case = Case("t001")
case.status = 'fail'
print case.__dict__
