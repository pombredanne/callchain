# -*- coding: utf-8 -*-
'''callchain lazy call and event chains tests'''

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from callchain.tests.mixins.man.queuing import MQMixin
from callchain.tests.mixins.auto.queuing import AQMixin
from callchain.tests.mixins.man.mapping import MMapQMixin
from callchain.tests.mixins.auto.mapping import AMapQMixin
from callchain.tests.mixins.man.ordering import MOrderQMixin
from callchain.tests.mixins.man.reducing import MReduceQMixin
from callchain.tests.mixins.auto.ordering import AOrderQMixin
from callchain.tests.mixins.man.filtering import MFilterQMixin
from callchain.tests.mixins.auto.reducing import AReduceQMixin
from callchain.tests.mixins.auto.filtering import AFilterQMixin

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


if __name__ == '__main__':
    unittest.main()
