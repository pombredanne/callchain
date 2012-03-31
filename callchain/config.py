# -*- coding: utf-8 -*-
'''callchain configuration'''

import logging

from callchain.settings import DefaultSettings


class Defaults(DefaultSettings):
    class log:
        # log level
        LEVEL = logging.DEBUG
        # default log formats
        DATE = '%a, %d %b %Y %H:%M:%S'
        # log entry format
        ENTRY = '%(name)s: %(asctime)s %(levelname)-4s %(message)s'

        class stream:
            ENABLED = True
            # redirect STDOUT to the logger?
            STDOUT = True
            # sets log level STDOUT is displayed under
            LEVEL = logging.DEBUG

        class email:
            ENABLED = False
            # mail server
            SERVER = ''
            # from email address
            FROM = ''
            # to email address
            TO = ''
            # email subject
            SUBJECT = ''

        class rotating:
            ENABLED = False
            # log file path
            FILE = ''
            # number of backups to keep
            BACKUPS = 1
            # interval to backup log file
            INTERVAL = 'h'

        class http:
            ENABLED = False
            # web server host
            HTTP = ''
            # web url
            URL = ''
            # http method
            METHOD = 'GET'

        class syslog:
            ENABLED = False
            # syslog host
            HOST = 'localhost'
            # syslog port
            PORT = 514
            # syslog facility
            FACILITY = 'LOG_USER'
