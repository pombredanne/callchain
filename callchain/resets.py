# -*- coding: utf-8 -*-
'''callchain resetables'''

from threading import local
from operator import setitem

from stuf.six import items
from stuf import frozenstuf
from stuf.utils import either, lazy
from stuf.utils import getcls, lazybase, exhaustmap


class ResetTypeMixin(object):

    '''`reset` descriptors that subclass `lazybase`'''

    def reset(self):
        '''reset previously accessed `lazybase` attributes'''
        this = vars(self)
        t = lambda x, y: x in this and isinstance(y, lazybase)
        exhaustmap(items(vars(getcls(self))), delattr, t)


class ResetLocalMixin(local):

    '''`reset` descriptors that subclass `lazybase`'''

    def reset(self):
        '''reset previously accessed `lazybase` attributes'''
        this = vars(self)
        t = lambda x, y: x in this and isinstance(y, lazybase)
        exhaustmap(items(vars(getcls(self))), delattr, t)
        
        
class CoreMixin(ResetLocalMixin):

    '''core mixin'''
    
    def __init__(self, root):
        '''
        init

        @param root: root chain
        '''
        super(CoreMixin, self).__init__()
        self._setup(root)

    @either
    def G(self):
        '''external application global settings'''
        return self.M.settings.final if self.M is not None else frozenstuf()
        

class ConfigMixin(CoreMixin):
    
    '''configuration access mixin'''
        
    @lazy
    def defaults(self):
        '''default settings by their lonesome'''
        return self.M.settings.defaults if self.M is not None else frozenstuf()

    @lazy
    def required(self):
        '''required settings by their lonesome'''
        return self.M.settings.required if self.M is not None else frozenstuf()
    
    def _defaults(self):
        '''reset attribute values'''
        this = self.__dict__
        self.exhaustmap(
            vars(self),
            lambda x, y: setitem(this, x.rstrip('_d'), y),
            lambda x: x[0].endswith('_d'),
        )
        
    def _setdefault(self, key, value):
        '''
        set default value for instance attribute

        @param key: attribute name
        @param value: attribute value
        '''
        self.__dict__[key] = self.__dict__[key + '_d'] = value
