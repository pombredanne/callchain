# -*- coding: utf-8 -*-
'''callchain lazy call and event chains tests'''

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from twoq.tests.mixins.auto.queuing import AQMixin
from twoq.tests.mixins.auto.mapping import AMapQMixin
from twoq.tests.mixins.auto.ordering import AOrderQMixin
from twoq.tests.mixins.auto.reducing import AReduceQMixin
from twoq.tests.mixins.auto.filtering import AFilterQMixin

from twoq.tests.mixins.man.queuing import MQMixin
from twoq.tests.mixins.man.mapping import MMapQMixin
from twoq.tests.mixins.man.ordering import MOrderQMixin
from twoq.tests.mixins.man.reducing import MReduceQMixin
from twoq.tests.mixins.man.filtering import MFilterQMixin

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
        from callchain.lazy.chain import lachainq
        return lachainq


class TestManChainQ(
    Manning, CallMixin, MQMixin, MFilterQMixin, MMapQMixin, MReduceQMixin,
    MOrderQMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.lazy.chain import lmchainq
        return lmchainq


if __name__ == '__main__':
    unittest.main()
