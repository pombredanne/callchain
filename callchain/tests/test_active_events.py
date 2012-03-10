# -*- coding: utf-8 -*-
'''callchain event chains test mixins'''

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from callchain.tests.mixins.auto.queuing import AQMixin
from callchain.tests.mixins.auto.mapping import AMapQMixin
from callchain.tests.mixins.auto.ordering import AOrderQMixin
from callchain.tests.mixins.auto.reducing import AReduceQMixin
from callchain.tests.mixins.auto.filtering import AFilterQMixin

from callchain.tests.mixins.man.manning import Manning
from callchain.tests.mixins.man.queuing import MQMixin
from callchain.tests.mixins.man.mapping import MMapQMixin
from callchain.tests.mixins.man.ordering import MOrderQMixin
from callchain.tests.mixins.man.reducing import MReduceQMixin
from callchain.tests.mixins.man.filtering import MFilterQMixin

from callchain.tests.mixins.chain import CallingMixin
from callchain.tests.mixins.event import EventChainMixin


class TestActiveAutoEventChain(
    unittest.TestCase, EventChainMixin, CallingMixin, AQMixin, AFilterQMixin,
    AMapQMixin, AReduceQMixin, AOrderQMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.active.chain import aaeventq
        return aaeventq


class TestActiveManEventChain(
    Manning, EventChainMixin, CallingMixin, MQMixin, MFilterQMixin,
    MMapQMixin, MReduceQMixin, MOrderQMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.active.chain import ameventq
        return ameventq


if __name__ == '__main__':
    unittest.main()
