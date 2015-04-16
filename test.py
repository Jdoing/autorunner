#!/usr/bin/python
import os, sys
from lib import GlobalSet
#from lib.TestRunner.Runner import Runner

db = [('db_host', '127.0.0.1'), ('db_port', '22'), ('db_user', 'root'), ('db_pass', 'rootroot')]

print map(lambda t : t[1], db)

print zip('abc', '123')
