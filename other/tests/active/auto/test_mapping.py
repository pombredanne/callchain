# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

#pylint: disable-msg=w0614,w0401
from twoq.tests.mixins.auto.mapping import *  # @UnusedWildImport
from twoq.tests.mixins.auto.queuing import AQMixin


class TestAutoMap(AQMixin, AMapQMixin):

    def setUp(self):
        from callchain.active.mapping import amaplink
        self.qclass = amaplink


class TestAutoMappingQ(unittest.TestCase, AQMixin, AMappingQMixin):

    def setUp(self):
        from callchain.active.mapping import amappinglink
        self.qclass = amappinglink


class TestAutoRepeatQ(unittest.TestCase, AQMixin, ARepeatQMixin):

    def setUp(self):
        from callchain.active.mapping import arepeatlink
        self.qclass = arepeatlink


class TestAutoDelayQ(unittest.TestCase, AQMixin, ADelayQMixin):

    def setUp(self):
        from callchain.active.mapping import adelaylink
        self.qclass = adelaylink


class TestSyncMap(AQMixin, AMapQMixin):

    def setUp(self):
        from callchain.active.mapping import smaplink
        self.qclass = smaplink


class TestSyncMappingQ(unittest.TestCase, AQMixin, AMappingQMixin):

    def setUp(self):
        from callchain.active.mapping import smappinglink
        self.qclass = smappinglink


class TestSyncRepeatQ(unittest.TestCase, AQMixin, ARepeatQMixin):

    def setUp(self):
        from callchain.active.mapping import srepeatlink
        self.qclass = srepeatlink


class TestSyncDelayQ(unittest.TestCase, AQMixin, ADelayQMixin):

    def setUp(self):
        from callchain.active.mapping import sdelaylink
        self.qclass = sdelaylink

if __name__ == '__main__':
    unittest.main()
