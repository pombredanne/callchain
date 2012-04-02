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
from callchain.tests.man.reducing import MReduceQMixin
from callchain.tests.auto.ordering import AOrderQMixin
from callchain.tests.man.filtering import MFilterQMixin
from callchain.tests.auto.reducing import AReduceQMixin
from callchain.tests.auto.filtering import AFilterQMixin

from callchain.tests.chain import CallMixin
from callchain.tests.manning import Manning


class TestAutoChainQ(
    unittest.TestCase, CallMixin, AQMixin, AFilterQMixin, AMapQMixin,
    AReduceQMixin, AOrderQMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.lazy_auto.chain import chainq
        return chainq


class TestAutoPriorityChainQ(
    unittest.TestCase, CallMixin, AQMixin, AFilterQMixin, AMapQMixin,
    AReduceQMixin, AOrderQMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.lazy_auto.chain import priorityq
        return priorityq


class TestManChainQ(
    Manning, CallMixin, MQMixin, MFilterQMixin, MMapQMixin, MReduceQMixin,
    MOrderQMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.lazy_man.chain import chainq
        return chainq


class TestManPriorityChainQ(
    Manning, CallMixin, MQMixin, MFilterQMixin, MMapQMixin, MReduceQMixin,
    MOrderQMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.lazy_man.chain import priorityq
        return priorityq


if __name__ == '__main__':
    unittest.main()
