# -*- coding: utf-8 -*-
'''callchain lazy call and event chains tests'''

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from callchain.tests.man.queuing import MQMixin
from callchain.tests.auto.queuing import AQMixin
from callchain.tests.man.mapping import MMapQMixin
from callchain.tests.auto.mapping import AMapQMixin
from callchain.tests.man.ordering import MOrderQMixin
from callchain.tests.auto.ordering import AOrderQMixin
from callchain.tests.man.reducing import MReduceQMixin
from callchain.tests.man.filtering import MFilterQMixin
from callchain.tests.auto.reducing import AReduceQMixin
from callchain.tests.auto.filtering import AFilterQMixin

from callchain.tests.manning import Manning
from callchain.tests.chain import CallMixin
from callchain.tests.event import EventChainMixin


class TestLazyAutoEventChain(
    unittest.TestCase, EventChainMixin, CallMixin, AQMixin, AFilterQMixin,
    AMapQMixin, AReduceQMixin, AOrderQMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.lazy_auto.event import eventq
        return eventq


class TestLazyManEventChain(
    Manning, EventChainMixin, MQMixin, MFilterQMixin, MMapQMixin,
    MReduceQMixin, MOrderQMixin, CallMixin,
):
    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.lazy_man.event import eventq
        return eventq


if __name__ == '__main__':
    unittest.main()
