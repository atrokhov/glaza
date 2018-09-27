# -*- coding: utf-8 -*-

import unittest
from parser import * 

class TestParser(unittest.TestCase):

    def test_parser_with_my_user(self):
        self.assertEqual(get_user_data("helloworld7743"), instagram_users_data.find_one({'username': 'helloworld7743'}))

    def test_parser_with_another_user(self):
        self.assertEqual(get_user_data("dawda"), instagram_users_data.find_one({'username': 'dawda'}))

    def test_parser_with_not_exicting_user(self):
        self.assertEqual(get_user_data("hagfjgafgafg"), None)

    def test_parser_with_one_user_two_times(self):
        get_user_data("helloworld7743")
        get_user_data("helloworld7743")
        self.assertEqual(instagram_users_data.find({'username': 'helloworld7743'}).count(), 1)

if __name__ == '__main__':
    unittest.main()