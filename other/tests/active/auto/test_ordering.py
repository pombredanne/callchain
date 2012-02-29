# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

#pylint: disable-msg=w0614,w0401
from twoq.tests.mixins.auto.ordering import *  # @UnusedWildImport
from twoq.tests.mixins.auto.queuing import AQMixin


class TestAutoOrderQ(unittest.TestCase, AQMixin, AOrderQMixin):

    def setUp(self):
        from callchain.active.ordering import aorderlink
        self.qclass = aorderlink


class TestAutoOrderingQ(unittest.TestCase, AQMixin, AOrderingQMixin):

    def setUp(self):
        from callchain.active.ordering import aorderinglink
        self.qclass = aorderinglink


class TestAutoRandomQ(unittest.TestCase, AQMixin, ARandomQMixin):

    def setUp(self):
        from callchain.active.ordering import arandomlink
        self.qclass = arandomlink


class TestSyncOrderQ(unittest.TestCase, AQMixin, AOrderQMixin):

    def setUp(self):
        from callchain.active.ordering import sorderlink
        self.qclass = sorderlink


class TestSyncOrderingQ(unittest.TestCase, AQMixin, AOrderingQMixin):

    def setUp(self):
        from callchain.active.ordering import sorderinglink
        self.qclass = sorderinglink


class TestSyncRandomQ(unittest.TestCase, AQMixin, ARandomQMixin):

    def setUp(self):
        from callchain.active.ordering import srandomlink
        self.qclass = srandomlink

if __name__ == '__main__':
    unittest.main()
