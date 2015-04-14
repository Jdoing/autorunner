#!/usr/bin/python
#coding=utf-8
import sys, os
sys.path = ["lib", "testcase"] + sys.path
import logging
import logging.config
import signal
if sys.hexversion < 0x02060000:
    print "Testrunner requires version 2.6+ of python"
    sys.exit()


log = logging.getLogger('SNTF')

def main():
	argParser = ArgParser()
	argParser = argParser.parse(sys.argv)
	
	
	
	


if __name__ == '__main__':
	child = os.fork()
	if child == 0:
		main()
	else:
		try:
			os.wait()
		except KeyboardInterrupt:
			print 'KeyBoardInterrupt'
			try:
				os.kill(child, signal.SIGKILL)
			except OSError:
				pass
			except OSError:
				pass
	sys.exit()

