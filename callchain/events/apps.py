# -*- coding: utf-8 -*-
'''event keys'''

from callchain.events.registry import Patterns

__all__ = ['events']


class events(Patterns):
    key = 'callchain.events.services.EEvent'
    # 1. before event
    before = 'callchain.events.services.EBefore'
    # 2. work event
    work = 'callchain.events.services.EWork'
    # 3. change event
    change = 'callchain.events.services.EChange'
    # 4. any event
    any = 'callchain.events.services.EAny'
    # 5. after event
    after = 'callchain.events.services.EAfter'
    # 6. problem event
    problem = 'callchain.events.services.EProblem'
    # 7. event that runs irrespective
    anyway = 'callchain.events.services.EAnyway'
