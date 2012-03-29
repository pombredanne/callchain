# -*- coding: utf-8 -*-
'''callchain compatibility'''

try:
    from Queue import PriorityQueue
except ImportError:
    from queue import PriorityQueue
