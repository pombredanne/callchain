# -*- coding: utf-8 -*-
'''callchain call mixins'''

from appspace.builders import Appspace
from stuf import frozenstuf, orderedstuf
from stuf.utils import either, lazy, lazy_class

from callchain.keys.core import NoServiceError

from callchain.mixins.resets import ResetLocalMixin


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
        '''enter context'''
        return self

    def __exit__(self, e, t, b):
        '''exit context'''
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
        '''consume call chain until exhausted'''
        return self.outextend(
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
            # 1. "before" event 2. "work" event
            self.trigger('before', 'work')
            # everything else
            super(EventCallMixin, self).commit()
            # 3. "change" event 4. "any" event 5. "after" event
            fire('change', 'any', 'after')
        except:
            # 6. "problem" event
            fire('problem')
        finally:
            # 7. event that runs "anyway"
            fire('anyway')
        return self

    def fire(self, *events):
        '''
        run calls bound to `events` **NOW**

        @param events: event labels
        '''
        self.ctx1(hard=True, workq='_util')
        with self._context():
            self._xtend(self._events(*events))
        self.ctx3(hard=True, inq='_util', clearout=False)
        with self._context():
            return self.outextend(c() for c in self._iterable).unswap()

    def queues(self, *events):
        '''
        ordered mapping of processing queues for `events`

        @param events: event labels
        '''
        return orderedstuf((e, self._eventq(e)) for e in events)
