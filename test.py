#!/usr/bin/python
import os, sys
import json

try:
    a = 1/0
except Exception, ex:
    print ex.__class__
    print ex.message
    print str(type(ex))
