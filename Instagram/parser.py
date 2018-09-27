import requests

def get_user_data(username):
    url = "https://apinsta.herokuapp.com/u/" + username
    r = requests.get(url).json()
    if r:
        media_urls = []
        follows = r['graphql']['user']['edge_follow']['count']
        followed_by = r['graphql']['user']['edge_followed_by']['count']
        media_count = r['graphql']['user']['edge_owner_to_timeline_media']['count']
        media = r['graphql']['user']['edge_owner_to_timeline_media']['edges']
        if media:
            for i in range(0, 3):
                media_urls.append("https://www.instagram.com/p/" + str(r['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['shortcode']))

        user_data = {
            'media_urls': media_urls,
            'follows': follows,
            'followed_by': followed_by,
            'media_count': media_count
        }

        return user_data
    else:
        return