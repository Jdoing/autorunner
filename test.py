#!/usr/bin/python
#coding=utf-8
import json
import os, sys, time
from os import path, fork, mkdir

class Parent(object):
    def __init__(self, filename):
        self.file = filename
        
class Child(Parent):
    def __init__(self, filename):
        ff = self.func(filename)
        super(Child, self).__init__(ff)
        
    def func(self, f):
        ff = str(f)
        return ff
#n好的
c = Child('你好')



print c.file
