# -*- coding: utf-8 -*-
'''reducing active linked call chain'''

from inspect import ismodule

from twoq.support import port
from twoq.mixins.reducing import MathMixin, TruthMixin, ReduceMixin

from twoq.active.mixins import AutoQMixin, ManQMixin, SyncQMixin

###############################################################################
## active math linked call chain ##############################################
###############################################################################


class amathchain(AutoQMixin, MathMixin):

    '''auto-balancing math linked call chain'''

mathchain = amathchain


class mmathchain(ManQMixin, MathMixin):

    '''manually balanced math linked call chain'''


class smathchain(SyncQMixin, MathMixin):

    '''autosynchronized math linked call chain'''

###############################################################################
## active truth linked call chain ####E########################################
###############################################################################


class atruthchain(AutoQMixin, TruthMixin):

    '''auto-balancing truth linked call chain'''

truthchain = atruthchain


class mtruthchain(ManQMixin, TruthMixin):

    '''manually balanced truth linked call chain'''


class struthchain(SyncQMixin, TruthMixin):

    '''autosynchronized truth linked call chain'''

###############################################################################
## reduce linked call chain ###################################################
###############################################################################


class areducechain(AutoQMixin, ReduceMixin):

    '''auto-balancing reduce linked call chain'''

reduceq = areducechain


class mreducechain(ManQMixin, ReduceMixin):

    '''manually balanced reduce linked call chain'''


class sreducechain(SyncQMixin, ReduceMixin):

    '''autosynchronized reduce linked call chain'''

__all__ = sorted(name for name, obj in port.items(locals()) if not any([
    name.startswith('_'), ismodule(obj),
]))
del ismodule
