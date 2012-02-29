# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

#pylint: disable-msg=w0614,w0401
from twoq.tests.mixins.auto.filtering import *  # @UnusedWildImport
from twoq.tests.mixins.auto.queuing import AQMixin


class TestAutoFilterQ(unittest.TestCase, AQMixin, AFilterQMixin):

    def setUp(self):
        self.maxDiff = None
        from callchain.active.filtering import afilterlink
        self.qclass = afilterlink


class TestAutoFilteringQ(unittest.TestCase, AQMixin, AFilteringQMixin):

    def setUp(self):
        from callchain.active.filtering import afilteringlink
        self.qclass = afilteringlink


class TestAutoSliceQ(unittest.TestCase, AQMixin, ASliceQMixin):

    def setUp(self):
        from callchain.active.filtering import aslicelink
        self.qclass = aslicelink


class TestAutoCollectQ(unittest.TestCase, AQMixin, ACollectQMixin):

    def setUp(self):
        self.maxDiff = None
        from callchain.active.filtering import acollectlink
        self.qclass = acollectlink


class TestAutoSetQ(unittest.TestCase, AQMixin, ASetQMixin):

    '''test automatically synchronized filtering'''

    def setUp(self):
        from callchain.active.filtering import asetlink
        self.qclass = asetlink


class TestSyncFilterQ(unittest.TestCase, AQMixin, AFilterQMixin):

    def setUp(self):
        self.maxDiff = None
        from callchain.active.filtering import sfilterlink
        self.qclass = sfilterlink


class TestSyncFilteringQ(unittest.TestCase, AQMixin, AFilteringQMixin):

    def setUp(self):
        from callchain.active.filtering import sfilteringlink
        self.qclass = sfilteringlink


class TestSyncSliceQ(unittest.TestCase, AQMixin, ASliceQMixin):

    def setUp(self):
        from callchain.active.filtering import sslicelink
        self.qclass = sslicelink


class TestSyncCollectQ(unittest.TestCase, AQMixin, ACollectQMixin):

    def setUp(self):
        self.maxDiff = None
        from callchain.active.filtering import scollectlink
        self.qclass = scollectlink


class TestSyncSetQ(unittest.TestCase, AQMixin, ASetQMixin):

    def setUp(self):
        from callchain.active.filtering import ssetlink
        self.qclass = ssetlink


if __name__ == '__main__':
    unittest.main()
