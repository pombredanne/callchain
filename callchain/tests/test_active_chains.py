# -*- coding: utf-8 -*-
'''callchain active call and event chains tests'''

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


class TestCallChain(unittest.TestCase, CallMixin):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.root.chain import callchain
        return callchain

#    def test_switch(self):
#        qclass = self._appconf
#        foo = qclass.switch('test', 'sublink').foo(3).bar(3).back()
#        foo.commit()
#        outgoing = foo.outgoing
#        self.assertEqual(outgoing.popleft(), 3.0)
#        self.assertEqual(outgoing.popleft(), 3.0)


class TestAutoChainQ(
    unittest.TestCase, AQMixin, AFilterQMixin, AMapQMixin, AReduceQMixin,
    AOrderQMixin, CallMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.active.chain import aachainq
        return aachainq


class TestManChainQ(
    Manning, MQMixin, MFilterQMixin, MMapQMixin, MReduceQMixin, MOrderQMixin,
    CallMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.active.chain import amchainq
        return amchainq


if __name__ == '__main__':
    unittest.main()
