# -*- coding: utf-8 -*-
'''callchain event chains tests'''


class EventChainMixin(object):

    @property
    def _appconf(self):
        from math import ceil, fabs
        from callchain.active.linked import chainlink
        from callchain.patterns import Pathways, Nameways
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

    def test_pure_on(self):
        from math import fsum, floor, sqrt
        self.qclass.on('before', floor, 3)
        self.qclass.on('before', fsum, [1.1, 1.1, 1.1]).on('before', sqrt, 4)
        self.qclass.on('work', floor, 3)
        self.qclass.on('work', fsum, [1.1, 1.1, 1.1]).on('work', sqrt, 4)
        self.qclass.on('any', floor, 3)
        self.qclass.on('any', fsum, [1.1, 1.1, 1.1]).on('any', sqrt, 4)
        self.qclass.on('after', floor, 3)
        self.qclass.on('after', fsum, [1.1, 1.1, 1.1]).on('after', sqrt, 4)
        self.qclass.on('anyway', floor, 3)
        self.qclass.on('anyway', fsum, [1.1, 1.1, 1.1]).on('anyway', sqrt, 4)
        self.qclass.commit()
        queues = self.qclass.queues('before', 'work', 'any', 'after', 'anyway')
        outgoing = queues['before']
        self.assertEqual(queues.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
        self.assertEqual(outgoing.popleft(), 2)
        outgoing = queues['work']
        self.assertEqual(queues.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
        self.assertEqual(outgoing.popleft(), 2)
        outgoing = queues['any']
        self.assertEqual(queues.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
        self.assertEqual(outgoing.popleft(), 2)
        outgoing = queues['after']
        self.assertEqual(queues.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
        self.assertEqual(outgoing.popleft(), 2)
        outgoing = queues['anyway']
        self.assertEqual(queues.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
        self.assertEqual(outgoing.popleft(), 2)

    def test_appspaced_on(self):
        qclass = self._appconf
        qclass.on('before', 'square', 'helpers', 3)
        qclass.on('before', 'formit', 'helpers',  [1.1, 1.1, 1.1]).on(
            'before', 'misc', 'subhelpers', 4
        )
        qclass.on('work', 'square', 'helpers', 3)
        qclass.on('work', 'formit', 'helpers',  [1.1, 1.1, 1.1]).on(
            'work', 'misc', 'subhelpers', 4
        )
        qclass.on('any', 'square', 'helpers', 3)
        qclass.on('any', 'formit', 'helpers',  [1.1, 1.1, 1.1]).on(
            'any', 'misc', 'subhelpers', 4
        )
        qclass.on('after', 'square', 'helpers', 3)
        qclass.on('after', 'formit', 'helpers',  [1.1, 1.1, 1.1]).on(
            'after', 'misc', 'subhelpers', 4
        )
        qclass.on('anyway', 'square', 'helpers', 3)
        qclass.on('anyway', 'formit', 'helpers',  [1.1, 1.1, 1.1]).on(
            'anyway', 'misc', 'subhelpers', 4
        )
        qclass.commit()
        queues = qclass.queues('before', 'work', 'any', 'after', 'anyway')
        outgoing = queues['before']
        self.assertEqual(queues.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
        self.assertEqual(outgoing.popleft(), 2)
        outgoing = queues['work']
        self.assertEqual(queues.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
        self.assertEqual(outgoing.popleft(), 2)
        outgoing = queues['any']
        self.assertEqual(queues.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
        self.assertEqual(outgoing.popleft(), 2)
        outgoing = queues['after']
        self.assertEqual(queues.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
        self.assertEqual(outgoing.popleft(), 2)
        outgoing = queues['anyway']
        self.assertEqual(queues.popleft(), 3.0)
        self.assertEqual(outgoing.popleft(), 3.3000000000000003)
        self.assertEqual(outgoing.popleft(), 2)
