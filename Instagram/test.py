# -*- coding: utf-8 -*-

import unittest
from parser import * 

client = MongoClient('localhost', 27017)
db = client.glaza

test_instagram_users_data = db.test_instagram_users_data

class TestParser(unittest.TestCase):

    def test_parser_with_my_user(self):
        result = {'username': 'helloworld7743', 'follows': 4, 'media_urls': ['https://www.instagram.com/p/BoLhd7HBtI4', 'https://www.instagram.com/p/BoLhcYHhnLg', 'https://www.instagram.com/p/BoLhZkhh72n'], 'media_count': 5, 'followed_by': 0}
        self.assertEqual(get_user_data("helloworld7743"), result)

    def test_parser_with_another_user(self):
        result = {'username': 'dawda', 'follows': 1395, 'media_urls': ['https://www.instagram.com/p/BoJDDKMAc4r', 'https://www.instagram.com/p/BnOUl5Fggan', 'https://www.instagram.com/p/Bm74PzaAKUI'], 'media_count': 85, 'followed_by': 2791}
        self.assertEqual(get_user_data("dawda"), result)

    def test_parser_with_not_exicting_user(self):
        self.assertIsNone(get_user_data("hagfjgafgafg"))

    def test_inserting_to_db(self):
        test_instagram_users_data.drop()
        test_instagram_users_data.insert_one(user_info('helloworld7743', db=test_instagram_users_data))
        self.assertEqual(test_instagram_users_data.count(), 1)
        
    def test_parser_with_one_user_two_times(self):
        test_instagram_users_data.drop()
        user_info("helloworld7743", db=test_instagram_users_data)
        user_info("helloworld7743", db=test_instagram_users_data)
        self.assertEqual(instagram_users_data.find({'username': 'helloworld7743'}).count(), 1)

    def test_parser_for_correct_inserting_to_db(self):
        test_instagram_users_data.drop()
        self.assertEqual(user_info("dawda", db=test_instagram_users_data), instagram_users_data.find_one({'username': 'dawda'}))


if __name__ == '__main__':
    unittest.main()