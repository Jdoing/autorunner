import os, sys
import logger

log1 = logger.get_logger()
log1.debug('log1 id is %d' % id(log1))
    
log2 = logger.get_logger()
log2.debug('log1 id is %d' % id(log2))

import logger
print 'end'

log2 = logger.get_logger()
log2.debug('log1 id is %d' % id(log2))
