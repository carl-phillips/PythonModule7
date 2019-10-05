import unittest
from unittest.mock import patch
import fun_with_collections.sort_and_search_list as sort_and_search_list


class TestList(unittest.TestCase):
    @patch('fun_with_collections.sort_and_search_list.search_list', return_value='3')
    def test_search_list(self, input):
        self.assertEqual(sort_and_search_list.search_list(), 3)

    @patch('fun_with_collections.sort_and_search_list.search_list', return_value='3')
    def test_search_list_not_found(self, input):
        self.assertEqual(sort_and_search_list.search_list(), -1)

if __name__ == '__main__':
    unittest.main()
