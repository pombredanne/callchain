# -*- coding: utf-8 -*-
'''event keys'''

__all__ = ['events']


class events(object):
    key = 'callchain.keys.event.EEvent'
    # 1. before event
    before = 'callchain.keys.event.EBefore'
    # 2. work event
    work = 'callchain.keys.event.EWork'
    # 3. change event
    change = 'callchain.keys.event.EChange'
    # 4. any event
    any = 'callchain.keys.event.EAny'
    # 5. after event
    after = 'callchain.keys.event.EAfter'
    # 6. problem event
    problem = 'callchain.keys.event.EProblem'
    # 7. event that runs irrespective
    anyway = 'callchain.keys.event.EAnyway'
