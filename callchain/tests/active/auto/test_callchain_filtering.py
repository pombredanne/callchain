# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

#pylint: disable-msg=w0614,w0401
from callchain.tests.mixins.auto.filtering import *  # @UnusedWildImport
from callchain.tests.mixins.auto.queuing import AQMixin


class TestAutoFilterQ(unittest.TestCase, AQMixin, AFilterQMixin):

    def setUp(self):
        self.maxDiff = None
        from callchain.active.auto.chains.filter import filterchain
        self.qclass = filterchain


class TestAutoSliceQ(unittest.TestCase, AQMixin, ASliceQMixin):

    def setUp(self):
        from callchain.active.auto.chains.filter import slicechain
        self.qclass = slicechain


class TestAutoCollectQ(unittest.TestCase, AQMixin, ACollectQMixin):

    def setUp(self):
        self.maxDiff = None
        from callchain.active.auto.chains.filter import collectchain
        self.qclass = collectchain


class TestAutoSetQ(unittest.TestCase, AQMixin, ASetQMixin):

    '''test automatically synchronized filtering'''

    def setUp(self):
        from callchain.active.auto.chains.filter import setchain
        self.qclass = setchain


if __name__ == '__main__':
    unittest.main()
