# -*- coding: utf-8 -*-
'''manual balancing call chain test mixins'''

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class Manning(unittest.TestCase):

    def _false_true_false(self, manq, expr, comp=None):
        self.assertFalse(manq.balanced)
        manq.sync()
        self.assertTrue(manq.balanced)
        if comp is not None:
            expr(manq.end(), comp)
        else:
            expr(manq.end())
        self.assertFalse(manq.balanced)

    def _true_true_false(self, manq, expr, comp=None):
        self.assertTrue(manq.balanced)
        manq.sync()
        self.assertTrue(manq.balanced)
        if comp is not None:
            expr(manq.end(), comp)
        else:
            expr(manq.end())
        self.assertFalse(manq.balanced)

    def _false_true_true(self, manq, expr, comp=None):
        self.assertFalse(manq.balanced)
        manq.sync()
        self.assertTrue(manq.balanced)
        if comp is not None:
            expr(manq.end(), comp)
        else:
            expr(manq.end())
        self.assertTrue(manq.balanced)
