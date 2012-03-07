# -*- coding: utf-8 -*-
'''callchain call chainlets'''

from appspace.keys import NoAppError

from callchain.octopus import Tentacle

from callchain.chains.core import LazyRootedQMixin, ActiveRootedQMixin

__all__ = ('ActiveChainletQMixin', 'LazyChainletQMixin', 'ChainletMixin')


class ChainletMixin(Tentacle):

    '''linked call chainlet mixin'''

    def _iget(self, label):
        '''
        silent internal switch back...

        @param label: appspaced thing label
        '''
        # fetch appspaced thing...
        try:
            return self._oiget(label)
        # ...or go back to root chain
        except NoAppError:
            return getattr(self.back(), label)

    _ciget = _iget

    def back(self):
        '''go back to root call chain'''
        return self.root.back(self)

    _oback = back


class ActiveChainletQMixin(ChainletMixin, ActiveRootedQMixin):

    '''active call chainlet queue mixin'''


class LazyChainletQMixin(ChainletMixin, LazyRootedQMixin):

    '''lazy linked call chainlet queue mixin'''
