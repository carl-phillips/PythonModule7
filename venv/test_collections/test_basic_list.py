import unittest
from unittest.mock import patch
import fun_with_collections.basic_list as basic_list


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='3')
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(), [3,3,3])

if __name__ == '__main__':
    unittest.main()
