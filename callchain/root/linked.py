# -*- coding: utf-8 -*-
'''root linked chains'''

from appspace.keys import appifies

from callchain.root.mixins import RootMixin
from callchain.keys.linked import KLinkedChain, KEventlink
from callchain.assembly.linked import LinkedChain, Eventlink


@appifies(KLinkedChain)
class chainlink(RootMixin, LinkedChain):

    '''root linked chain'''


@appifies(KEventlink)
class eventlink(RootMixin, Eventlink):

    '''root linked event chain'''
