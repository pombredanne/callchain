# -*- coding: utf-8 -*-
'''callchain active call and event chains tests'''


try:
    import unittest2 as unittest
except ImportError:
    import unittest

from callchain.tests.mixins.chain import CallingMixin

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


class TestCallChain(unittest.TestCase, CallingMixin):

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
    AOrderQMixin, CallingMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.active.chain import aachainq
        return aachainq


class TestManChainQ(
    Manning, MQMixin, MFilterQMixin, MMapQMixin, MReduceQMixin, MOrderQMixin,
    CallingMixin,
):

    def setUp(self):
        self.qclass = self._makeone()

    @property
    def _makeone(self):
        from callchain.active.chain import amchainq
        return amchainq


if __name__ == '__main__':
    unittest.main()
