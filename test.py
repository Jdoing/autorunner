#!/usr/bin/python
import os, sys
import json

#from lib.TestRunner.Runner import Runner
line = 'ExampleTest.Basic.ComputerTest.CalculatorTest.test_add, params={"x":2, "y":3}'
string = 'params={"x":2, "y":3}'
split_string = string.split('=', 1)

j_str = json.loads(split_string[1])

print j_str
