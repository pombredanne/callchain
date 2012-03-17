# -*- coding: utf-8 -*-
'''event services'''

__all__ = ['events']


class events(object):
    key = 'callchain.services.event.EEvent'
    # 1. before event
    before = 'callchain.services.event.EBefore'
    # 2. work event
    work = 'callchain.services.event.EWork'
    # 3. change event
    change = 'callchain.services.event.EChange'
    # 4. any event
    any = 'callchain.services.event.EAny'
    # 5. after event
    after = 'callchain.services.event.EAfter'
    # 6. problem event
    problem = 'callchain.services.event.EProblem'
    # 7. event that runs irrespective
    anyway = 'callchain.services.event.EAnyway'
