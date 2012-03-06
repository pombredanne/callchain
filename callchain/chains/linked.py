# -*- coding: utf-8 -*-
'''call chains queue mixins'''

from appspace.keys import NoAppError

from callchain.octopus import Tentacle

from callchain.chains.core import QMixin, LoneMixin

__all__ = ('ActiveLinkQMixin', 'LazyLinkQMixin', 'linked')


class _LinkedMixin(Tentacle):

    '''linked call chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(_LinkedMixin, self).__init__(root)
        self._setup_chain()

    def _iget(self, label):
        '''
        silent internal switch back...

        @param label: appspaced thing label
        '''
        # fetch appspaced thing...
        try:
            return self._oiget(label)
        #...or return to root chain
        except NoAppError:
            return getattr(self.back(), label)

    _ciget = _iget

    def back(self):
        '''return to root call chain'''
        return self.root.back(self)

    _oback = back


class _LinkedQMixin(_LinkedMixin, QMixin):

    '''linked call chain queue mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(_LinkedQMixin, self).__init__(root)
        # sync with root callable
        self._call = root._call
        # sync with root postitional arguments
        self._args = root._args
        # sync with root keyword arguments
        self._kw = root._kw


class chainlink(_LinkedMixin, LoneMixin):

    '''linked call chain'''


class ActiveLinkQMixin(_LinkedQMixin):

    '''active linked call chain queue mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(ActiveLinkQMixin, self).__init__(root)
        # sync with root incoming things
        self._inextend(root.incoming)
        # sync with root outgoing things
        self._outextend(root.outgoing)


class LazyLinkQMixin(_LinkedQMixin):

    '''lazy linked call chain queue mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(LazyLinkQMixin, self).__init__(root)
        # sync with root incoming things
        self.incoming = root.incoming
        # sync with root outgoing things
        self.outgoing = root.outgoing
