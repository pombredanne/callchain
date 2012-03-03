# -*- coding: utf-8 -*-
'''callchain manually balanced event chain tests'''

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from callchain.tests.mixins.man.manning import Manning
from callchain.tests.mixins.man.queuing import MQMixin
from callchain.tests.mixins.man.mapping import MMapQMixin
from callchain.tests.mixins.man.ordering import MOrderQMixin
from callchain.tests.mixins.man.reducing import MReduceQMixin
from callchain.tests.mixins.man.filtering import MFilterQMixin


class TestManQ(
    Manning, MQMixin, MFilterQMixin, MMapQMixin, MReduceQMixin, MOrderQMixin,
):

    def setUp(self):
        from callchain.active.man.events.chain import eventchain
        self.qclass = eventchain()

if __name__ == '__main__':
    unittest.main()
