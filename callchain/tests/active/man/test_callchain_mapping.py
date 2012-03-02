# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

#pylint: disable-msg=w0614,w0401
from callchain.tests.mixins.man.mapping import *  # @UnusedWildImport
from callchain.tests.mixins.man.manning import Manning
from callchain.tests.mixins.man.queuing import MQMixin


class TestManMap(Manning, MQMixin, MMapQMixin):

    def setUp(self):
        from callchain.active.man.chains.map import mapchain
        self.qclass = mapchain


class TestManRepeatQ(
    Manning, MQMixin, MRepeatQMixin
):

    def setUp(self):
        from callchain.active.man.chains.map import repeatchain
        self.qclass = repeatchain


class TestManDelayQ(Manning, MQMixin, MDelayQMixin):

    def setUp(self):
        from callchain.active.man.chains.map import delaychain
        self.qclass = delaychain


if __name__ == '__main__':
    unittest.main()
