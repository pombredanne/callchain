# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

#pylint: disable-msg=w0614,w0401
from callchain.tests.mixins.auto.mapping import *  # @UnusedWildImport
from callchain.tests.mixins.auto.queuing import AQMixin


class TestAutoMap(AQMixin, AMapQMixin):

    def setUp(self):
        from callchain.active.auto.chains.map import mapchain
        self.qclass = mapchain()


class TestAutoRepeatQ(unittest.TestCase, AQMixin, ARepeatQMixin):

    def setUp(self):
        from callchain.active.auto.chains.map import repeatchain
        self.qclass = repeatchain()


class TestAutoDelayQ(unittest.TestCase, AQMixin, ADelayQMixin):

    def setUp(self):
        from callchain.active.auto.chains.map import delaychain
        self.qclass = delaychain()

if __name__ == '__main__':
    unittest.main()
