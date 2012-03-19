# -*- coding: utf-8 -*-
'''callchain callchain test mixins'''

from collections import deque


class CallMixin(object):

    @property
    def _appconf(self):
        from callchain.patterns import Pathways, Nameways
        from callchain.linked import chainlink
        from math import ceil, fabs
        class testlink(chainlink): #@IgnorePep8
            def foo(self, x):
                self.callchain(ceil, x)
                return self
            def bar(self, x): #@IgnorePep8
                self.callchain(fabs, x)
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
        self.qclass.callchain(floor, 3)
        (self.qclass
        .callchain(fsum, [1.1, 1.1, 1.1])
        .callchain(sqrt, 4))
        self.qclass.commit()
        outgoing = deque(i for i in self.qclass.results())
        self.assertEqual(outgoing.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
        self.assertEqual(outgoing.popleft(), 2)

    def test_appspace_calls(self):
        qclass = self._appconf
        qclass.callchain('square', 'helpers', 3).callchain('misc', 'subhelpers', 4)
        qclass.callchain('formit', 'helpers', [1.1, 1.1, 1.1])
        qclass.commit()
        outgoing = deque(i for i in qclass.results())
        self.assertEqual(outgoing.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 2)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
