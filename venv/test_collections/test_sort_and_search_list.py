import unittest
from unittest.mock import patch
import fun_with_collections.sort_and_search_list as sort_and_search_list


class TestList(unittest.TestCase):
    @patch('builtins.input', side_effect='3')
    def test_search_list(self, mock_input):
        result = sort_and_search_list.search_list()
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect='6')
    def test_search_list_not_found(self, mock_input):
        result = sort_and_search_list.search_list()
        self.assertEqual(result, -1)

    def test_sort_list(self):
        self.assertEqual(sort_and_search_list.sort_list([2,1,3,4]), [1,2,3,4])

if __name__ == '__main__':
    unittest.main()
