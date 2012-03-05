# -*- coding: utf-8 -*-
'''call chains queue mixins'''

from callchain.chains.mixins import BaseMixin, LinkMixin, ChainMixin


class _BaseQMixin(BaseMixin):

    '''chain queue mixin'''

    def clear(self):
        '''clear every thing'''
        self._oclear()
        self._cclear()
        return self

    _cclear = clear

    def tap(self, call, key=False):
        '''
        add call

        @param call: callable or appspace label
        @param key: linked call chain key (default: False)
        '''
        # reset postitional arguments
        self._args = ()
        # reset keyword arguments
        self._kw = {}
        # set current application
        isstring = self.port.isstring
        self._call = self._M.get(call, key) if isstring(call) else call
        return self

    _ctap = tap


class LinkQMixin(LinkMixin, _BaseQMixin):

    '''linked call chain queue mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(LinkQMixin, self).__init__(root)
        # sync with root callable
        self._call = root._call
        # sync with root postitional arguments
        self._args = root._args
        # sync with root keyword arguments
        self._kw = root._kw


class ChainQMixin(ChainMixin, _BaseQMixin):

    '''call chain queue mixin'''

    def back(self, link):
        '''
        return from linked call chain

        @param link: linked call chain
        '''
        self._oback(link)
        # sync with link callable
        self._call = link._call
        # sync with link postitional arguments
        self._args = link._args
        # sync with link keyword arguments
        self._kw = link._kw
        return self

    _cback = back


class ActiveLinkMixin(LinkQMixin):

    '''linked call chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        super(ActiveLinkMixin, self).__init__(root)
        # sync with root incoming things
        self._inextend(root.incoming)
        # sync with root outgoing things
        self._outextend(root.outgoing)


class ActiveChainMixin(ChainQMixin):

    '''call chain mixin'''

    def __call__(self, *args):
        '''load args into incoming thing'''
        # clear call chain and queues
        self.clear()
        # extend incoming things
        self._inextend(args)
        return self

    def back(self, link):
        '''
        return from linked call chain

        @param link: linked call chain
        '''
        self._cback(link)
        # sync with link incoming things
        self._inclear()
        self._inextend(link.incoming)
        # sync with link outgoing things
        self._outclear()
        self._outextend(link.outgoing)
        return self

    _ccback = back


class LazyLinkMixin(LinkQMixin):

    '''linked call chain mixin'''

    def __init__(self, root):
        '''
        init

        @param root: root call chain
        '''
        # sync with root incoming things
        self.incoming = root.incoming
        # sync with root outgoing things
        self.outgoing = root.outgoing
        super(LazyLinkMixin, self).__init__(root)


class LazyChainMixin(ChainQMixin):

    '''call chain mixin'''

    def __call__(self, *args):
        '''load args into incoming thing'''
        # clear call chain and queues
        self.clear()
        # extend incoming things
        self.incoming = iter([args[0]]) if len(args) == 1 else iter(args)
        return self

    def back(self, link):
        '''
        return from linked call chain

        @param link: linked call chain
        '''
        self._cback(link)
        # sync with link incoming things
        self.incoming = link.incoming
        # sync with link outgoing things
        self.outgoing = link.outgoing
        return self

    _ccback = back
