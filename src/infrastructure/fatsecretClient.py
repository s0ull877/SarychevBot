import json
import requests

from settings import get_settings
from logger import get_logger

settings = get_settings()
logger = get_logger()

class FatSecretClientOAuthv2:

    def __init__(self, client_id, client_secret):

        self.client_id= client_id
        self.client_secret = client_secret

        token = self._get_access_token()

        if token is not None:
            self.access_token = token

        logger.warning('No access token for fatsecret Oauth2')


    def _get_access_token(self):

        data = {
            "grant_type": "client_credentials",
            "scope": "basic"
        }

        response = requests.post('https://oauth.fatsecret.com/connect/token', data=data, auth=(self.client_id, self.client_secret))
        if response.status_code == 200:

            data = json.loads(response.text)
            return data.get('access_token')

        else:
            return None


    def image_recognition(self, image_b64, eaten_foods: list[dict] | None=None, lang_code: str='RU-ru') -> dict | None:

        region, language = tuple(lang_code.split('-'))

        data = {
            "image_b64": image_b64,
            "region": region,
            "language": language,
            "include_food_data": True,
        }

        if eaten_foods:
            data['eaten_foods'] = eaten_foods


        response = requests.post('https://platform.fatsecret.com/rest/image-recognition/v1', data=data, headers={'Authorization': f'Bearer {self.access_token}'})

        pass



clientV2 = FatSecretClientOAuthv2(settings.fatsecret_id, settings.fatsecret_key)
