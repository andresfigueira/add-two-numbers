import unittest
from ..add_two_numbers.add_two_numbers import add_two_numbers


class TestAddTwoNumbers(unittest.TestCase):
    def test_should_work_if_both_lists_have_integer_elements_with_equal_length(self):
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        answer = add_two_numbers(l1, l2)
        self.assertEqual(answer, [8, 0, 7])

    def test_should_return_none_if_one_list_has_larger_length(self):
        l1 = [1, 3, 5, 9]
        l2 = [5, 1, 2]
        answer = add_two_numbers(l1, l2)
        self.assertEqual(answer, None)

    def test_should_return_none_if_one_element_is_not_integer(self):
        l1 = [1, 3, 5]
        l2 = [5, 1, "2"]
        answer = add_two_numbers(l1, l2)
        self.assertEqual(answer, None)

    def test_should_return_empty_array_if_both_lists_are_empty(self):
        l1 = []
        l2 = []
        answer = add_two_numbers(l1, l2)
        self.assertEqual(answer, [])
