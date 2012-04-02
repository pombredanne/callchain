# -*- coding: utf-8 -*-
'''callchain contrib keys'''

#from appspace.keys import Attribute

from callchain.services.queue import KService


class KLogger(KService):

    '''logging key'''

#    logger = Attribute('the logger')

    def debug(msg):  # @NoSelf
        '''log debug message'''

    def warning(msg):  # @NoSelf
        '''log warning message'''

    def info(msg):  # @NoSelf
        '''log info message'''

    def error(msg):  # @NoSelf
        '''log error message'''

    def critical(msg):  # @NoSelf
        '''log critical message'''

    def exception(msg):  # @NoSelf
        '''log exception message'''
