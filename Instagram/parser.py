import requests
import re
from bs4 import BeautifulSoup
from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client.glaza

instagram_users_data = db.instagram_users_data

def get_user_data(username):
    url = 'https://www.instagram.com/' + username
    db_check = instagram_users_data.find_one({"username": username})
    r = requests.get(url)
    if r:
        soup = BeautifulSoup(r.content, 'html.parser')
        script = soup.find('script', text=re.compile('window._sharedData'))
        json_text = re.search(r'^\s*window\._sharedData\s*=\s*({.*?})\s*;\s*$', script.string, flags=re.DOTALL | re.MULTILINE).group(1)
        data = json.loads(json_text)['entry_data']['ProfilePage'][0]['graphql']['user']

        media_urls = []
        follows = data['edge_follow']['count']
        followed_by = data['edge_followed_by']['count']
        media_count = data['edge_owner_to_timeline_media']['count']
        media = data['edge_owner_to_timeline_media']['edges']

        if media:
            for i in range(0, 3):
                media_urls.append("https://www.instagram.com/p/" + str(media[i]['node']['shortcode']))

        user_data = {
            'username':username,
            'media_urls': media_urls,
            'follows': follows,
            'followed_by': followed_by,
            'media_count': media_count
        }

        return user_data


def user_info(username, db=instagram_users_data):
    db_check = instagram_users_data.find_one({"username": username})
    if not db_check:
        instagram_users_data.insert_one(get_user_data(username))
        return db_check
    else:
        return db_check
