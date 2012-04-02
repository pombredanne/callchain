# -*- coding: utf-8 -*-
'''callchain active call and event chains tests'''

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
from callchain.tests.auto.reducing import AReduceQMixin
from callchain.tests.man.filtering import MFilterQMixin
from callchain.tests.auto.filtering import AFilterQMixin

from callchain.tests.chain import CallMixin
from callchain.tests.manning import Manning


class TestAutoChainQ(
    unittest.TestCase, AQMixin, AFilterQMixin, AMapQMixin, AReduceQMixin,
    AOrderQMixin, CallMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.active_auto.chain import chainq
        return chainq


class TestAutoPriorityChainQ(
    unittest.TestCase, AQMixin, AFilterQMixin, AMapQMixin, AReduceQMixin,
    AOrderQMixin, CallMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.active_auto.chain import priorityq
        return priorityq


class TestManChainQ(
    Manning, MQMixin, MFilterQMixin, MMapQMixin, MReduceQMixin, MOrderQMixin,
    CallMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.active_man.chain import chainq
        return chainq


class TestManPriorityChainQ(
    Manning, MQMixin, MFilterQMixin, MMapQMixin, MReduceQMixin, MOrderQMixin,
    CallMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.active_man.chain import priorityq
        return priorityq


if __name__ == '__main__':
    unittest.main()
