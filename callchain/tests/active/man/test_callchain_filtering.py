# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

#pylint: disable-msg=w0614,w0401
from callchain.tests.mixins.man.filtering import *  # @UnusedWildImport
from callchain.tests.mixins.man.manning import Manning
from callchain.tests.mixins.man.queuing import MQMixin


class TestManFilterQ(Manning, MFilterQMixin):

    def setUp(self):
        self.maxDiff = None
        from callchain.active.man.chains.filter import filterchain
        self.qclass = filterchain


class TestManSliceQ(Manning, MQMixin, MSliceQMixin):

    def setUp(self):
        from callchain.active.man.chains.filter import slicechain
        self.qclass = slicechain


class TestManCollectQ(Manning, MQMixin, MCollectQMixin):

    def setUp(self):
        from callchain.active.man.chains.filter import collectchain
        self.qclass = collectchain


class TestManSetQ(Manning, MQMixin, MSetQMixin):

    def setUp(self):
        from callchain.active.man.chains.filter import setchain
        self.qclass = setchain


if __name__ == '__main__':
    unittest.main()
