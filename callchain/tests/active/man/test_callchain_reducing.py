# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

#pylint: disable-msg=w0614,w0401
from callchain.tests.mixins.man.reducing import *  # @UnusedWildImport
from callchain.tests.mixins.man.manning import Manning
from callchain.tests.mixins.man.queuing import MQMixin


class TestManReduceQ(Manning, MQMixin, MReduceQMixin):

    def setUp(self):
        from callchain.active.man.chains.reduce import reducechain
        self.qclass = reducechain()


class TestManMathQ(Manning, MQMixin, MMathQMixin):

    def setUp(self):
        from callchain.active.man.chains.reduce import mathchain
        self.qclass = mathchain()


class TestManTruthQ(Manning, MQMixin, MTruthQMixin):

    def setUp(self):
        from callchain.active.man.chains.reduce import truthchain
        self.qclass = truthchain()


if __name__ == '__main__':
    unittest.main()
