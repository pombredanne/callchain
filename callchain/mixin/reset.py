# -*- coding: utf-8 -*-
'''callchain reset mixins'''

from threading import local

from stuf.six import items
from stuf.utils import getcls, lazybase


class ResetTypeMixin(object):

    '''
    mixin to add a ".reset()" method to methods decorated with "lazybase"

    By default, lazy attributes, once computed, are static. If they happen to
    depend on other parts of an object and those parts change, their values may
    be out of sync.

    This class offers a ".reset()" method that an instance can call its state
    has _changed and invalidate all their lazy attributes. Once reset() is
    called, all lazy attributes are reset to original format and their accessor
    functions can be triggered again.
    '''

    def reset(self):
        '''reset accessed lazy attributes'''
        instdict = vars(self)
        classdict = vars(getcls(self))
        # To reset them, we simply remove them from the instance dict. At that
        # point, it's as if they had never been computed. On the next access,
        # the accessor function from the parent class will be called, simply
        # because that's how the python descriptor protocol works.
        for key, value in items(classdict):
            if all([key in instdict, isinstance(value, lazybase)]):
                delattr(self, key)

    _rreset = reset


class ResetLocalMixin(local):

    '''thread `local` version versione of `ResetTypeMixin`'''

    def reset(self):
        '''reset previously accessed `lazybase` attributes'''
        instdict = vars(self)
        classdict = vars(getcls(self))
        for key, value in items(classdict):
            if all([key in instdict, isinstance(value, lazybase)]):
                delattr(self, key)

    _rreset = reset
