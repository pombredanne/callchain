try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestPatterns(unittest.TestCase):

    @staticmethod
    def _make_multiple():
        from math import fabs
        from appspace import Patterns, class_patterns

        class helpers(Patterns):
            square = 'math.sqrt'
            fabulous = fabs
            formit = 're.match'
        return class_patterns('helpers', helpers)

    def test_attr_multiple(self):
        plug = self._make_multiple()
        self.assertEqual(plug.helpers.square, plug['helpers']['square'])
        self.assertEqual(plug.helpers.fabulous, plug['helpers']['fabulous'])
        self.assertEqual(plug.helpers.formit, plug['helpers']['formit'])
        self.assertEqual(plug.helpers.lower, plug['helpers']['lower'])
        self.assertEqual(plug.helpers.upper, plug['helpers']['upper'])
        self.assertEqual(plug.helpers.store, plug['helpers']['store'])

    def test_identity_namespace(self):
        from appspace.builders import Appspace
        app = self._make_multiple()
        self.assertIsInstance(app.helpers, Appspace)

    def test_identity_multiple(self):
        from re import match
        from math import sqrt, fabs
        plug = self._make_multiple()
        self.assert_(plug.helpers.square is sqrt)
        self.assert_(plug.helpers.fabulous is fabs)
        self.assert_(plug.helpers.formit is match)

    def test_call2_multiple(self):
        from re import match
        from math import sqrt, fabs
        plug = self._make_multiple()
        self.assertEqual(plug.helpers.square(2), sqrt(2))
        self.assertEqual(plug.helpers.fabulous(2), fabs(2))
        self.assertEqual(
            plug.helpers.formit('2', '2').string, match('2', '2').string
        )
