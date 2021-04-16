import unittest

from sort import sort

class SortTest(unittest.TestCase):
    def test_empty_list(self):
        inputArr = []

        output = sort(inputArr)

        assert output == []

    def test_single_element_list(self):
        inputArr = [1]

        output = sort(inputArr)

        assert output == [1]
