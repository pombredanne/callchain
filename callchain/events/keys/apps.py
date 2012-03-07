# -*- coding: utf-8 -*-
'''event keys'''

__all__ = ['events']


class events(object):
    key = 'callchain.events.keys.events.EEvent'
    # 1. before event
    before = 'callchain.events.keys.events.EBefore'
    # 2. work event
    work = 'callchain.events.keys.events.EWork'
    # 3. change event
    change = 'callchain.events.keys.events.EChange'
    # 4. any event
    any = 'callchain.events.keys.events.EAny'
    # 5. after event
    after = 'callchain.events.keys.events.EAfter'
    # 6. problem event
    problem = 'callchain.events.keys.events.EProblem'
    # 7. event that runs irrespective
    anyway = 'callchain.events.keys.events.EAnyway'
