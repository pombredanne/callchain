# -*- coding: utf-8 -*-
'''manual balancing call chain test mixins'''

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class Manning(unittest.TestCase):

    def _false_true_false(self, manq, expr, comp=None):
        manq = manq.back()
        self.assertFalse(manq.balanced)
        manq.sync()
        self.assertTrue(manq.balanced)
        if comp is not None:
            expr(manq.value(), comp)
        else:
            expr(manq.value())
        self.assertFalse(manq.balanced)

    def _true_true_false(self, manq, expr, comp=None):
        manq = manq.back()
        self.assertTrue(manq.balanced)
        manq.sync()
        self.assertTrue(manq.balanced)
        if comp is not None:
            expr(manq.value(), comp)
        else:
            expr(manq.value())
        self.assertFalse(manq.balanced)

    def _false_true_true(self, manq, expr, comp=None):
        manq = manq.back()
        self.assertFalse(manq.balanced)
        manq.sync()
        self.assertTrue(manq.balanced)
        if comp is not None:
            expr(manq.value(), comp)
        else:
            expr(manq.value())
        self.assertTrue(manq.balanced)
