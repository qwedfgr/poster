import os

import requests


def post_image_and_text(image_path, text):
    fb_group_id = os.getenv('FB_GROUP_ID')
    fb_token = os.getenv('FB_TOKEN')
    url = f'https://graph.facebook.com/v5.0/{fb_group_id}/photos/'

    params = {'caption': text, 'access_token': fb_token}

    with open(image_path, 'rb') as file:
        response = requests.post(url, params, files={'photo': file})
    response.raise_for_status()
