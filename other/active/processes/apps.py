# -*- coding: utf-8 -*-
'''callchain events appconf'''

from appspace import Namespace

from octopus import Pathways

__all__ = ['callchain']


class callchain(Pathways):

    class auto(Namespace):

        class filtering(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''

        class mapping(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''

        class ordering(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''

        class queuing(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''

        class reducing(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''

    class man(Namespace):

        class filtering(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''

        class mapping(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''

        class ordering(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''

        class queuing(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''

        class reducing(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''

    class sync(Namespace):

        class filtering(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''

        class mapping(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''

        class ordering(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''

        class queuing(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''

        class reducing(Namespace):
            context = ''
            event = ''
            process = ''
            workflow = ''
