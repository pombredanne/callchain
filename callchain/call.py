# -*- coding: utf-8 -*-
'''callchain calling mixins'''

from collections import deque
from functools import partial

from appspace.builders import Appspace
from stuf.utils import lazy, lazy_class, either
from twoq.support import port, isstring
from stuf import frozenstuf, orderedstuf

from callchain.keys.octopus import NoServiceError
from callchain.mixins import ChainingMixin, EventsMixin


class CallingMixin(ChainingMixin):

    '''calling mixin'''

    def _setup_chain(self):
        '''setup call chain'''
        _chain = deque()
        # call chain right extend
        self._cxtend = _chain.extend
        # call chain right append
        self._cappend = _chain.append
        # call chain left append
        self._cappendleft = _chain.appendleft
        # call chain left pop
        self._cpopleft = _chain.popleft
        # call chain clear
        self._cclear = _chain.clear
        # call chain
        self._chain = _chain

    _osetup_chain = _setup_chain

    def chain(self, call, key=False, *args, **kw):
        '''
        add callable or appspaced callable to call chain, partializing it with
        any passed arguments

        @param call: callable or application label
        @param key: appspace key label (default: False)
        '''
        if not isstring(call):
            call = partial(call, *(key,) + args, **kw)
        else:
            call = partial(self.M.get(call, key), *args, **kw)
        self._cappend(call)
        return self

    _ochain = chain


class QCallingMixin(CallingMixin):

    '''queued chain mixin'''

    def clear(self):
        '''clear all queues'''
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
        self._call = self._M.get(call, key) if isstring(call) else call
        return self

    _ctap = tap


class ECallingMixin(EventsMixin, CallingMixin):

    '''event chain execution mixin'''

    def commit(self):
        '''run event chain'''
        try:
            trigger = self.trigger
            fire = self.fire
            # 1. before event
            trigger('before')
            # 2. work event
            trigger('work')
            # everything else
            self._ocommit()
            # 3. change event
            fire('change')
            # 4. any event
            fire('any')
            # 5. after event
            fire('after')
        except:
            # 6. problem event
            fire('problem')
        finally:
            # 7. event that runs irrespective
            fire('anyway')
        return self

    def queues(self, *events):
        '''
        ordered mapping of processing queues for `events`

        @param *events: event labels
        '''
        return orderedstuf((e, self._eventq(e).outgoing) for e in events)


class CallMixin(CallingMixin):

    '''root chain mixin'''

    def _iget(self, label):
        '''
        silent internal switch to...

        @param label: appspaced thing label
        '''
        try:
            # look up internally linked call chains...
            _M = self._M
            key = _M.service(label)
            return getattr(_M.get(key, key)(self), label)
        except NoServiceError:
            # ...or lookup other appspace things
            return self._oiget(label)

    _ciget = _iget

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

    def switch(self, label, key=False):
        '''
        overt switch to linked call chain from external appspace

        @param label: linked call chain label
        @param key: linked call chain chain key (default: False)
        '''
        return self.M.get(label, key)(self)

    _oswitch = switch

    class Meta:
        pass
