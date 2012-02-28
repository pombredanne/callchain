# -*- coding: utf-8 -*-
'''twoq active reducing linked event chains'''

from inspect import ismodule

from twoq.support import port
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from twoq.active.mixins import AutoQMixin, ManQMixin, SyncQMixin

###############################################################################
## active math linked event chains ############################################
###############################################################################


class amathlink(AutoQMixin, MathMixin):

    '''auto-balancing math linked event chain'''

mathlink = amathlink


class mmathlink(ManQMixin, MathMixin):

    '''manually balanced math linked event chain'''


class smathlink(SyncQMixin, MathMixin):

    '''autosynchronized math linked event chain'''

###############################################################################
## active truth linked event chains ####E######################################
###############################################################################


class atruthlink(AutoQMixin, TruthMixin):

    '''auto-balancing truth linked event chain'''

truthlink = atruthlink


class mtruthlink(ManQMixin, TruthMixin):

    '''manually balanced truth linked event chain'''


class struthlink(SyncQMixin, TruthMixin):

    '''autosynchronized truth linked event chain'''

###############################################################################
## reduce linked event chains #################################################
###############################################################################


class areducelink(AutoQMixin, ReduceMixin):

    '''auto-balancing reduce linked event chain'''

reducelink = areducelink


class mreducelink(ManQMixin, ReduceMixin):

    '''manually balanced reduce linked event chain'''


class sreducelink(SyncQMixin, ReduceMixin):

    '''autosynchronized reduce linked event chain'''

__all__ = sorted(name for name, obj in port.items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
del ismodule
