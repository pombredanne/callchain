# -*- coding: utf-8 -*-
'''callchain pathwayss'''

from twoq import port
from appspace.keys import ConfigurationError
from appspace.spaces import Patterns, patterns

from callchain.core.managers import Manager

__all__ = ['Pathways']


class Pathways(Patterns):

    '''patterns for appspace'''

    _manager = Manager

    @classmethod
    def appspace(cls, pattern, required=None, defaults=None, *args, **kw):
        '''
        build new appspace

        @param pattern: pattern configuration class or appspace label
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        # from appspace configuration class...
        if issubclass(pattern, Patterns):
            return pattern.build(required, defaults)
        # from label and arguments...
        elif port.isstring(pattern) and args:
            manager = patterns(pattern, *args, **kw)
            if any([required is not None, defaults is not None]):
                cls.settings(manager, required, defaults)
            return manager
        raise ConfigurationError('patterns not found')

    # pylint: disable-msg=w0221
    @classmethod
    def build(cls, required=None, defaults=None):
        '''
        build manager configuration from class

        @param required: required settings
        @param defaults: default settings
        '''
        manager = super(Pathways, cls).build()
        if any([required is not None, defaults is not None]):
            cls.settings(manager, required, defaults)
        return manager
    # pylint: enable-msg=w0221

    @classmethod
    def settings(cls, manager, required=None, defaults=None):
        '''
        attach settings to class

        @param required: required settings
        @param defaults: default settings
        '''
        manager.settings.required = required
        manager.settings.defaults = defaults
