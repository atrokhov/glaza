from instagram.client import InstagramAPI
from tokens import access_token, client_secret

class InstagrammData:

    def __init__(self, access_token, client_secret, user_id):
        self.access_token = access_token
        self.client_secret = client_secret
        self.user_id = user_id
        self.api = InstagramAPI(access_token=access_token, client_secret=client_secret)

    def user_follows(self):
        return self.api.user(user_id=self.user_id).counts['follows']

    def user_followed_by(self):
        return self.api.user(user_id=self.user_id).counts['followed_by']

    def user_recent_media(self):
        return self.api.user_recent_media(user_id=self.user_id, count=3)
