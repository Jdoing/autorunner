#!/usr/bin/python
#coding=utf-8
import json
import os, sys, time
import re
sys.path = ["lib", "testcase"] + sys.path
import unittest

class Parent(object):
    def __init__(self):
        self.x = 10
    
    def func1(self):
        pass
        
class Child(Parent):
    static_data = 123
    def __init__(self):
        #ff = self.func(filename)
        self.y = 10
        super(Child, self).__init__()
        
    def func2(self):
        pass
'''
c = Child()
print dir(c)
print '-' * 40
print dir(Child)
print '-' * 40
print Child.__dict__
print '-' * 40
print c.__dict__
'''

class Runner(object):
    def getTestCaseByDir(self, dir_path):
        if not os.path.isdir(dir_path):
            print '[%s] is not dir' % dir_path
            sys.exit(1)
        
        is_in_package = True
        cases = []
        for dirname, subdirs, files in os.walk(dir_path):
            if '__init__.py' not in files:
                is_in_package = False
            for test_file in files:
                if re.match(r'^[_a-z]\w*\.py$', test_file, re.IGNORECASE) and test_file != '__init__.py':
                    file_name = os.path.join(dirname, test_file)                    
                    cases.extend(self.getTestCaseFromFile(file_name, is_in_package))
        return cases

    def getTestCaseFromFile(self, file_name, is_in_package = False):
        module = None
            #module_name = test_moudle[test_moudle.rfind('.') + 1:]
            #module = __import__(test_moudle, globals(), locals(), [module_name], -1)
            #print 'module_name is: ', module_name
        if is_in_package:
            try:
                test_module = file_name[:file_name.rfind('.py')].replace(os.sep, '.')
                __import__(test_module)
                
            except ImportError:
                print 'can not import this module: %s' % test_module
            else:
                module = sys.modules[test_module]
        else:
            import imp
            module_name = os.path.splitext(os.path.basename(file_name))[0]
            search_path = os.path.abspath(os.path.dirname(file_name))
            print 'file_name is: ', file_name
            print 'module_name is:', module_name
            print 'search_path is:', search_path
            
            fp, pathname, desc = imp.find_module(module_name, [search_path])
            try:
                module = imp.load_module(module_name, fp, pathname, desc)
            finally:
                if fp:
                    fp.close()
        

        #print getattr(module, 'CalculatorTest')
        '''
        print module
        #print 'name is:', dir(module.__name__)
        print 'name is:', module.__name__
        #print 'path is:', module.__path__
        print 'dir is:', dir(module)
        #print module.__dict__
        #print module.Basic
        '''
        return self.getTestCaseFromModule(module)
    
    def getTestCaseFromModule(self, module):
        for name in dir(module):
            obj = getattr(module, name)
            try:
                if isinstance(obj, type) and issubclass(obj, unittest.TestCase):
                    return self.getTestCaseFromClass(obj)
            except TypeError:
                pass
    
    def getTestCaseFromClass(self, class_obj):
        #cases = []
        prefix = 'test'
        def is_test_method(func_name):
            return func_name.startswith(prefix) and hasattr(getattr(class_obj, func_name), '__call__')
        #print dir(class_obj)
        cases = filter(is_test_method, dir(class_obj))
        return cases
        
    
runner = Runner()
print 'case is: %s' % runner.getTestCaseByDir('ExampleTest')



if 0:
    import ExampleTest.Basic.ComputerTest as m
    print dir(m)


