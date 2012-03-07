# -*- coding: utf-8 -*-
'''callchain active call and event chains tests'''


class CallChainMixin(object):

    @property
    def _appconf(self):
        from callchain.octopus import Pathways, Nameways
        class helpers(Pathways): #@IgnorePep8
            square = 'math.floor'
            formit = 'math.fsum'
            class subhelpers(Nameways): #@IgnorePep8
                misc = 'math.sqrt'
        return self._makeone(helpers)

    def test_pure_calls(self):
        from math import fsum, floor, sqrt
        self.qclass.chain(floor, 3)
        self.qclass.chain(fsum, [1.1, 1.1, 1.1])
        self.qclass.chain(sqrt, 4)
        self.qclass.commit()
        outgoing = self.qclass.outgoing
        self.assertEqual(outgoing.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
        self.assertEqual(outgoing.popleft(), 2)

    def test_appspace_calls(self):
        qclass = self._appconf
        qclass.chain('square', 'helpers', 3)
        qclass.chain('formit', 'helpers', [1.1, 1.1, 1.1])
        qclass.chain('misc', 'subhelpers', 4)
        qclass.commit()
        outgoing = qclass.outgoing
        self.assertEqual(outgoing.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
        self.assertEqual(outgoing.popleft(), 2)
