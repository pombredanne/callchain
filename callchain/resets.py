# -*- coding: utf-8 -*-
'''callchain resetables'''

from threading import local

from stuf.six import items
from stuf.utils import getcls, lazybase, exhaustmap


class ResetTypeMixin(object):

    '''`reset` descriptors that subclass `lazybase`'''

    def reset(self):
        '''reset previously accessed `lazybase` attributes'''
        this = vars(self)
        t = lambda x, y: x in this and isinstance(y, lazybase)
        exhaustmap(items(vars(getcls(self))), delattr, t)

    _rreset = reset


class ResetLocalMixin(local):

    '''`reset` descriptors that subclass `lazybase`'''

    def reset(self):
        '''reset previously accessed `lazybase` attributes'''
        this = vars(self)
        t = lambda x, y: x in this and isinstance(y, lazybase)
        exhaustmap(items(vars(getcls(self))), delattr, t)

    _rreset = reset