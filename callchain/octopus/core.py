# -*- coding: utf-8 -*-
'''appspace octopus'''

from twoq.support import port
from stuf.core import frozenstuf
from appspace.builders import Appspace
from stuf.utils import lazy, lazy_class, either
from appspace.keys import AppLookupError, NoAppError

from callchain.octopus.patterns import Pathways
from callchain.octopus.resets import ResetLocalMixin

__all__ = ('Octopus', 'Tentacle', 'inside')


class InsideMixin(object):

    '''configure internal appspace mixin'''

    def __init__(self, pattern, required=None, defaults=None, *args, **kw):
        '''
        init

        @param pattern: pattern configuration class or appspace label
        @param required: required global settings (default: None)
        @param defaults: default global settings (default: None)
        '''
        self.pattern = pattern
        self.required = required
        self.defaults = defaults
        self.args = args
        self.kw = kw

    def __call__(self, that):
        # internal appspace manager
        that._M = Pathways.appspace(
            self.pattern,
            self.required,
            self.defaults,
            *self.args,
            **self.kw
        )
        # lock internal appspace global settings
        that._M.settings.lock()
        # set internal appspace global settings
        that._G = that._M.settings.final
        return that

    _ocall = __call__


inside = InsideMixin


class _Octopus(ResetLocalMixin):

    '''octopus base'''

    def __getattr__(self, label):
        try:
            return object.__getattribute__(self, label)
        except AttributeError:
            return self._iget(label)

    def _iget(self, label):
        '''
        load item from appspace

        @param label: potential appspace label
        '''
        _M = self._M
        try:
            item = _M.get(label, _M._current)
        except AppLookupError:
            try:
                # lookup namespace
                _M.namespace(label)
            except AppLookupError:
                raise NoAppError(label)
            else:
                # temporarily swap primary label
                _M._current = label
                return self
        else:
            # ensure current label set back to default
            _M._current = _M._root
            return item

    _oiget = _iget

    @either
    def L(self):
        '''local external appspace settings'''
        return self._M.localize(self) if self._M is not None else frozenstuf()

    @lazy_class
    def port(self):
        '''python 2.x <-> python 3.x compatibility helper'''
        return port

    @lazy
    def space(self):
        '''external appspace interface'''
        return Appspace(self.M) if self.M is not None else None


class Octopus(_Octopus):

    '''appspace octopus'''

    def __init__(self, pattern=None, required=None, defaults=None, **kw):
        '''
        init

        @param pattern: pattern configuration or appspace label (default: None)
        @param required: required settings (default: None)
        @param defaults: default settings (default: None)
        '''
        super(Octopus, self).__init__()
        if pattern is not None:
            # external appspace
            self.M = Pathways.appspace(pattern, required, defaults)
            # freeze external appspace global settings
            self.M.freeze(kw)
        else:
            self.M = None

    @either
    def G(self):
        '''external application global settings'''
        return self.M.settings.final if self.M is not None else frozenstuf()


class Tentacle(_Octopus):

    '''appspace tentacle'''

    def __init__(self, root):
        '''
        init

        @param root: root object
        '''
        super(Tentacle, self).__init__()
        # root object
        self.root = root
        # root internal appspace manager
        self._M = root._M
        # root internal global settings
        self._G = root._G
        # root external appspace manager
        self.M = root.M
        # root external global settings
        self.G = root.G if self.M else None
