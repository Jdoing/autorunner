import os, sys

def _getWorkdir():
    curPath = os.path.abspath(__file__)
    updir = os.path.dirname(curPath)
    return os.path.dirname(updir)
    
workdir = _getWorkdir()


__all__ = [workdir, ]
