# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

#pylint: disable-msg=w0614,w0401
from callchain.tests.mixins.man.ordering import *  # @UnusedWildImport
from callchain.tests.mixins.man.manning import Manning
from callchain.tests.mixins.man.queuing import MQMixin


class TestManOrderQ(Manning, MQMixin, MOrderQMixin):

    def setUp(self):
        from callchain.active.man.chains.order import orderchain
        self.qclass = orderchain()


class TestManRandomQ(Manning, MQMixin, MRandomQMixin):

    def setUp(self):
        from callchain.active.man.chains.order import randomchain
        self.qclass = randomchain()

if __name__ == '__main__':
    unittest.main()
