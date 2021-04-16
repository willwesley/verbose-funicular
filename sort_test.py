import unittest

from sort import sort

class SortTest(unittest.TestCase):
    def test_empty_list(self):
        inputArr = []

        output = sort(inputArr)

        assert output == []