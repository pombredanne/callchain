# -*- coding: utf-8 -*-
'''callchain call chainlets'''

from appspace.keys import NoAppError

from callchain.octopus import Tentacle

from callchain.chains.core import QMixin, LoneMixin

__all__ = ('ActiveChainletQMixin', 'LazyChainletQMixin', 'linked')


class _ChainletMixin(Tentacle):

    '''linked call chainlet mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(_ChainletMixin, self).__init__(root)
        self._setup_chain()

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


class _ChainletQMixin(_ChainletMixin, QMixin):

    '''linked call chain queue mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(_ChainletQMixin, self).__init__(root)
        # sync with root callable
        self._call = root._call
        # sync with root postitional arguments
        self._args = root._args
        # sync with root keyword arguments
        self._kw = root._kw


class chainlet(_ChainletMixin, LoneMixin):

    '''linked call chainlet'''


class ActiveChainletQMixin(_ChainletQMixin):

    '''active call chainlet queue mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(ActiveChainletQMixin, self).__init__(root)
        # sync with root incoming things
        self._inextend(root.incoming)
        # sync with root outgoing things
        self._outextend(root.outgoing)


class LazyChainletQMixin(_ChainletQMixin):

    '''lazy linked call chainlet queue mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(LazyChainletQMixin, self).__init__(root)
        # sync with root incoming things
        self.incoming = root.incoming
        # sync with root outgoing things
        self.outgoing = root.outgoing
