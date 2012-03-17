# -*- coding: utf-8 -*-
'''root linked chains'''

from appspace.keys import appifies

from callchain.keys.linked import KLinkedChain, KEventLink
from callchain.assembly.linked import LinkedChain, EventLink

from callchain.root.mixins import RootableMixin


@appifies(KLinkedChain)
class chainlink(RootableMixin, LinkedChain):

    '''root linked call chain'''


@appifies(KEventLink)
class eventlink(RootableMixin, EventLink):

    '''root linked event chain'''
