# -*- coding: utf-8 -*-
'''callchain chainlet mixins'''

from appspace.keys import NoAppError

from callchain.rooted import RootedMixin, RootedQMixin, ERootedMixin,\
    RootedChainMixin


class Chainlet(RootedMixin):

    '''callchain chainlet'''

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


class ChainletCallMixin(Chainlet, RootedChainMixin):

    '''queued chainlet mixin'''


class ChainletQMixin(ChainletCallMixin, RootedQMixin):

    '''queued chainlet mixin'''


class EChainletMixin(ChainletCallMixin, ERootedMixin):

    '''event chainlet mixin'''
