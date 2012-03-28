# -*- coding: utf-8 -*-
'''callchain call mixins'''

from stuf import frozenstuf
from appspace.builders import Appspace
from stuf.utils import OrderedDict, either, lazy, lazy_class

from callchain.resets import ResetLocalMixin
from callchain.keys.base import NoServiceError


class CallMixin(ResetLocalMixin):

    '''chain execution mixin'''

    @either
    def L(self):
        '''local settings'''
        return self._M.localize(self) if self._M is not None else frozenstuf()

    @lazy_class
    def port(self):
        '''python 2.x <-> python 3.x porting helper'''
        from twoq.support import port
        return port

    @lazy
    def space(self):
        '''external appspace interface'''
        return Appspace(self.M) if self.M is not None else None

    def __enter__(self):
        '''enter execution context'''
        return self

    def __exit__(self, e, t, b):
        '''exit execution context'''
        # invoke call chain
        self.commit()

    def _load(self, label):
        '''
        silent internal switch to...

        @param label: label of appspaced thing
        '''
        try:
            # look up internal appspaced linked call chain...
            _M = self._M
            key = _M.service(label)
            return getattr(_M.get(key, key)(self), label)
        except NoServiceError:
            # ...or lookup other appspaced thing
            return super(CallMixin, self)._load(label)

    def switch(self, label, key=False):
        '''
        overt switch to linked chain configured in external appspace

        @param label: linked chain label
        @param key: linked chain chain key (default: False)
        '''
        return self.M.get(label, key)(self)

    def commit(self):
        '''consume call chain'''
        with self.ctx3():
            return self._xtend(
                c() for c in self.iterexcept(self._chain.popleft, IndexError)
            )

    class Meta:
        pass


class EventCallMixin(CallMixin):

    '''event execution mixin'''

    def commit(self):
        '''run event chain'''
        fire = self.fire
        try:
            #TODO: consider how this piles up
            # 1. "before" event 2. "work" event
            fire('before', 'work')
            # everything else
            super(EventCallMixin, self).commit()
            # 3. "change" event 4. "any" event 5. "after" event
            fire('change', 'any', 'after')
        except:
            # 6. "problem" event
            fire('problem')
        finally:
            # 7. event that runs "anyway"
            return fire('anyway')

    def fire(self, *events):
        '''
        run calls bound to `events` **NOW**

        @param *events: event labels
        '''
        with self.ctx1(workq='_work'):
            self.exhaustcall(
                lambda x: x(), self._xtend(self._events(*events))._iterable,
            )
            return self

    def queues(self, *events):
        '''
        ordered mapping of processing queues for `events`

        @param *events: event labels
        '''
        return OrderedDict((e, self._eventq(e)) for e in events)
