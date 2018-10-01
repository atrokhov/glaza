import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.glaza

instagram_users_data = db.instagram_users_data

def get_user_data(username):
    url = "https://apinsta.herokuapp.com/u/" + username
    db_check = instagram_users_data.find_one({"username": username})
    if not db_check:
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        script = soup.find('script', text=re.compile('window._sharedData'))
        json_text = re.search(r'^\s*window\._sharedData\s*=\s*({.*?})\s*;\s*$',
                      script.string, flags=re.DOTALL | re.MULTILINE).group(1)
        data = json.loads(json_text)['entry_data']['ProfilePage'][0]['graphql']['user']
        if r:
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

            instagram_users_data.insert_one(user_data)

            return db_check
        else:
            return db_check
    else:
        return db_check