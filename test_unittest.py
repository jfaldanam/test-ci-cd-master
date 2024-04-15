import unittest

from main import make_upper_case

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(make_upper_case("foo"), 'FOO')