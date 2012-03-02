# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

#pylint: disable-msg=w0614,w0401
from callchain.tests.mixins.auto.reducing import *  # @UnusedWildImport
from callchain.tests.mixins.auto.queuing import AQMixin


class TestAutoReduceQ(unittest.TestCase, AQMixin, AReduceQMixin):

    def setUp(self):
        from callchain.active.auto.chains.reduce import reducechain
        self.qclass = reducechain


class TestAutoMathQ(unittest.TestCase, AQMixin, AMathQMixin):

    def setUp(self):
        from callchain.active.auto.chains.reduce import mathchain
        self.qclass = mathchain


class TestAutoTruthQ(unittest.TestCase, AQMixin, ATruthQMixin):

    def setUp(self):
        from callchain.active.auto.chains.reduce import truthchain
        self.qclass = truthchain


if __name__ == '__main__':
    unittest.main()
