import unittest

from hello import HelloClass

class HelloClassTest(unittest.TestCase):
    def setUp(self):
        self.subject = HelloClass()

    def assertListEqual(self, actual, expected):
        assert len(actual) == len(expected)
        assert all([a == b for a, b in zip(actual, expected)])

    def test_for_smoke(self):
        self.subject.say_hi()

        self.assertListEqual([1,2,3],[1,2,3])
