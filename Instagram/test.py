# -*- coding: utf-8 -*-

import unittest
from parser import * 

class TestParser(unittest.TestCase):

    def test_parser_with_my_user(self):
        result = {'follows': 3, 'media_urls': ['https://www.instagram.com/p/BoLhd7HBtI4', 'https://www.instagram.com/p/BoLhcYHhnLg', 'https://www.instagram.com/p/BoLhZkhh72n'], 'media_count': 5, 'followed_by': 0}

        self.assertEqual(get_user_data("helloworld7743"), result)

    def test_parser_with_another_user(self):
        result = {'follows': 1395, 'media_urls': [], 'media_count': 85, 'followed_by': 2794}

        self.assertEqual(get_user_data("dawda"), result)

    def test_parser_with_not_exicting_user(self):
        self.assertEqual(get_user_data("hagfjgafgafg"), None)

if __name__ == '__main__':
    unittest.main()