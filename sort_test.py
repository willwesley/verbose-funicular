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

    def test_two_element_sorted_list(self):
        inputArr = [1,2]

        output = sort(inputArr)

        assert output == [1,2]

    def test_two_element_unsorted_list(self):
        inputArr = [2,1]

        output = sort(inputArr)

        assert output == [1,2]

    def test_three_element_unsorted_list(self):
        inputArr = [2,1,3]

        output = sort(inputArr)

        assert output == [1,2,3]

    def test_three_element_sorted_list(self):
        inputArr = [1,2,3]

        output = sort(inputArr)

        assert output == [1,2,3]

