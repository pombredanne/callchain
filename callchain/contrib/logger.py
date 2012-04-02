# -*- coding: utf-8 -*-
'''callchain logging'''

import sys
import logging
from logging.handlers import HTTPHandler, SysLogHandler
from logging.handlers import TimedRotatingFileHandler, SMTPHandler

from appspace import appifies
from stuf.utils import clsname

from callchain.core import CoreMixin
from callchain.chain import BranchMixin, ChainletMixin

from callchain.contrib.keys import KLogger


class _LogStdout(object):

    '''file-like object for sending stdout output to a logger.'''

    def __init__(self, logger, level=logging.DEBUG):
        '''
        build stdout logger

        @param logger: logger
        @param level: logging level (default: `logging.DEBUG`
        '''
        # Set logger level
        if level == logging.DEBUG:
            self.logger = logger.debug
        elif level == logging.CRITICAL:
            self.logger = logger.critical
        elif level == logging.ERROR:
            self.logger = logger.error
        elif level == logging.WARNING:
            self.logger = logger.warning
        elif level == logging.INFO:
            self.logger = logger.info

    def write(self, msg):
        '''Writes non-empty strings to logger.'''
        if msg.lstrip().rstrip() != '':
            self.logger(msg)


@appifies(KLogger)
class loglet(ChainletMixin, BranchMixin, CoreMixin):

    '''logging chainlet'''

    def _setup(self, root):
        '''
        build logger

        @param root: root chain
        '''
        super(loglet, self)._setup(root)
        settings = self._G.log
        self.logger = logging.getLogger(settings.get('NAME', clsname(root)))
        # set logging level
        self.logger.setLevel(settings.LEVEL)
        # log formatter
        format = logging.Formatter(
            # log entry format
            settings.ENTRY,
            # date format
            settings.DATE,
        )
        # coroutine to setup log handlers
        def setlog(thislog): #@IgnorePep8
            thislog.setFormatter(format)
            self.logger.addHandler(thislog)
        # log to STDOUT
        if settings.stream:
            setlog(logging.StreamHandler())
            # redirect STDOUT to the logger
            if settings.stream.STDOUT:
                # sets log level STDOUT is displayed under
                sys.stdout = _LogStdout(self.logger, settings.stream.LEVEL)
        # log to a rotating file that with periodic backup deletions
        if settings.rotating.ENABLED:
            setlog(TimedRotatingFileHandler(
                # log file path
                settings.rotating.PATH,
                # interval to backup log file
                settings.rotating.INTERVAL,
                # number of backups to keep
                settings.rotating.BACKUPS,
            ))
        # email log entries to an email address
        if settings.email.ENABLED:
            setlog(SMTPHandler(
                # mail server
                settings.email.HOST,
                # from email address
                settings.email.FROM,
                # to email address
                settings.email.TO,
                # email subject
                settings.email.SUBJECT,
            ))
        # send log entries to a web server
        if settings.http.ENABLED:
            setlog(HTTPHandler(
                # web server host
                settings.http.HOST,
                # web url
                settings.http.URL,
                # http method
                settings.http.METHOD,
            ))
        # send log entries to syslog
        if settings.syslog.ENABLED:
            setlog(SysLogHandler(
                # syslog host
                (settings.syslog.HOST, settings.syslog.PORT),
                # syslog user
                settings.syslog.FACILITY,
            ))
        assert self.logger.handlers, 'configure at least one logging handler'

    def debug(self, msg):
        '''log debug message'''
        self.logger.debug(msg)
        return self

    def warning(self, msg):
        '''log warning message'''
        self.logger.warning(msg)
        return self

    def info(self, msg):
        '''log info message'''
        self.logger.info(msg)
        return self

    def error(self, msg):
        '''log error message'''
        self.logger.error(msg)
        return self

    def critical(self, msg):
        '''log critical message'''
        self.logger.critical(msg)
        return self

    def exception(self, msg):
        '''log exception message'''
        self.logger.exception(msg)
        return self
