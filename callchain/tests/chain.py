# -*- coding: utf-8 -*-
'''callchain test mixins'''

from collections import deque


class CallMixin(object):

    @property
    def _appconf(self):
        from callchain.patterns import Pathways, Nameways
        from callchain.lazy_auto.chainlet import chainlink
        from math import ceil, fabs
        class testlink(chainlink): #@IgnorePep8
            def foo(self, x):
                self.chain(ceil, x)
                return self
            def bar(self, x): #@IgnorePep8
                self.chain(fabs, x)
                return self
        class helpers(Pathways): #@IgnorePep8
            square = 'math.floor'
            formit = 'math.fsum'
            class subhelpers(Nameways): #@IgnorePep8
                misc = 'math.sqrt'
            class sublink(Nameways): #@IgnorePep8
                test = testlink
        return self._makeone(helpers)

    def test_pure_calls(self):
        from math import fsum, floor, sqrt
        (self.qclass.chain(floor, 3).chain(
            fsum, [1.1, 1.1, 1.1]
        ).chain(sqrt, 4))
        self.qclass.commit()
        outgoing = deque(self.qclass)
        self.assertEqual(outgoing.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
        self.assertEqual(outgoing.popleft(), 2)

    def test_appspace_calls(self):
        qclass = self._appconf
        qclass.chain('square', 'helpers', 3).chain('misc', 'subhelpers', 4)
        qclass.chain('formit', 'helpers', [1.1, 1.1, 1.1])
        qclass.commit()
        outgoing = deque(qclass)
        self.assertEqual(outgoing.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 2)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
