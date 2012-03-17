# -*- coding: utf-8 -*-
'''callchain patterns'''

from twoq import port
from stuf.six import strings
from stuf.utils import exhaust, imap
from appspace.utils import lazyimport
from appspace.keys import ConfigurationError, ANamespace
from appspace.spaces import Branch, Namespace, Patterns, patterns

from callchain.managers import Manager
from callchain.keys.core import KService

__all__ = ['Pathways', 'Branchways', 'Nameways']


class Pathways(Patterns):

    '''callchain patterns'''

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


class _PatternsMixin(object):

    @classmethod
    def _key(cls, label, manager):
        try:
            # lazily load key
            key = cls.key
            if isinstance(key, strings):
                key = lazyimport(key)
            # register class key
            ez_register = manager.ez_register
            ez_register(ANamespace, label, key)
            exhaust(imap(
                lambda x: ez_register(KService, x, label),
                iter(key.names(True)),
            ))
        except AttributeError:
            key = manager.key(ANamespace, label)


class Branchways(_PatternsMixin, Branch):

    '''branch ways'''


class Nameways(_PatternsMixin, Namespace):

    '''name ways'''
