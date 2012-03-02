# -*- coding: utf-8 -*-
'''callchain auto-balancing call chain tests'''

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from callchain.tests.mixins.auto.queuing import AQMixin
from callchain.tests.mixins.auto.mapping import AMapQMixin
from callchain.tests.mixins.auto.ordering import AOrderQMixin
from callchain.tests.mixins.auto.reducing import AReduceQMixin
from callchain.tests.mixins.auto.filtering import AFilterQMixin


class TestAutoQ(
    unittest.TestCase, AQMixin, AFilterQMixin, AMapQMixin, AReduceQMixin,
    AOrderQMixin,
):

    def setUp(self):
        from callchain.active.auto.chains.chain import callchain
        self.qclass = callchain


if __name__ == '__main__':
    unittest.main()
