# -*- coding: utf-8 -*-
'''event keys'''

from callchain.events.registry import Patterns

__all__ = ['events']


class events(Patterns):
    key = 'callchain.events.apps.EEvent'
    # 1. before event
    before = 'callchain.events.apps.EBefore'
    # 2. work event
    work = 'callchain.events.apps.EWork'
    # 3. change event
    change = 'callchain.events.apps.EChange'
    # 4. any event
    any = 'callchain.events.apps.EAny'
    # 5. after event
    after = 'callchain.events.apps.EAfter'
    # 6. problem event
    problem = 'callchain.events.apps.EProblem'
    # 7. event that runs irrespective
    anyway = 'callchain.events.apps.EAnyway'
