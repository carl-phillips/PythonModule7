import unittest
from unittest.mock import patch
import fun_with_collections.basic_list as basic_list
import fun_with_collections.basic_list_exception as basic_list_exception

class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list_exception.get_input', return_value=-3)
    def test_make_list_below_range(self, input):
        self.assertLess(basic_list_exception.get_input(), 1)

    @patch('fun_with_collections.basic_list_exception.get_input', return_value=55)
    def test_make_list_above_range(self, input):
        self.assertGreater(basic_list_exception.get_input(), 50)

    @patch('fun_with_collections.basic_list_exception.make_list', return_value=3)
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(), [3,3,3])

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.get_input()


if __name__ == '__main__':
    unittest.main()
