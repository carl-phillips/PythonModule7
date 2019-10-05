import unittest
import array as arr
from unittest.mock import patch
import fun_with_collections.sort_and_search_array as sort_and_search_array


class TestList(unittest.TestCase):
    @patch('builtins.input', side_effect='3')
    def test_search_array(self, mock_input):
        result = sort_and_search_array.search_array()
        self.assertEqual(result, 1)

    @patch('builtins.input', side_effect='9')
    def test_search_array_not_found(self, mock_input):
        result = sort_and_search_array.search_array()
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
