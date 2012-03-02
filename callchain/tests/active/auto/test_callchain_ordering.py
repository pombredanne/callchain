# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

#pylint: disable-msg=w0614,w0401
from callchain.tests.mixins.auto.ordering import *  # @UnusedWildImport
from callchain.tests.mixins.auto.queuing import AQMixin


class TestAutoOrderQ(unittest.TestCase, AQMixin, AOrderQMixin):

    def setUp(self):
        from callchain.active.auto.chains.order import orderchain
        self.qclass = orderchain


class TestAutoRandomQ(unittest.TestCase, AQMixin, ARandomQMixin):

    def setUp(self):
        from callchain.active.auto.chains.order import randomchain
        self.qclass = randomchain

if __name__ == '__main__':
    unittest.main()
