# -*- coding: utf-8 -*-
'''reset mixins'''

from threading import local

from stuf.six import items
from stuf.utils import getcls, lazybase, exhaustmap


class ResetTypeMixin(object):

    '''
    mixin to add ``reset`` method to descriptors inheriting from ``lazybase``
    '''

    def reset(self):
        '''reset previously accessed ``lazybase`` attributes'''
        this = vars(self)
        that = vars(getcls(self))
        t = lambda x, y: x in this and isinstance(y, lazybase)
        exhaustmap(items(that), delattr, t)

    _rreset = reset


class ResetLocalMixin(local):

    '''
    mixin to add ``reset`` method to descriptors inheriting from ``lazybase``
    (thread ``local`` version)
    '''

    def reset(self):
        '''reset previously accessed ``lazybase`` attributes'''
        this = vars(self)
        that = vars(getcls(self))
        t = lambda x, y: x in this and isinstance(y, lazybase)
        exhaustmap(items(that), delattr, t)

    _rreset = reset
