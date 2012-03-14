# -*- coding: utf-8 -*-
'''root linked chains'''

from appspace.keys import appifies

from callchain.keys.linked import KLinkedChain, KEventlink
from callchain.assembly.linked import LinkedChain, Eventlink

from callchain.root.mixins import RootMixin


@appifies(KLinkedChain)
class chainlink(RootMixin, LinkedChain):

    '''root linked call chain'''


@appifies(KEventlink)
class eventlink(RootMixin, Eventlink):

    '''root linked event chain'''
