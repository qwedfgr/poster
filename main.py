import os

from dotenv import load_dotenv

import fb
import tg
import vk


def main():
    load_dotenv()
    photos_path = os.getenv('PHOTOS_PATH')
    text = os.getenv('TEXT')

    fb_group_id = os.getenv('FB_GROUP_ID')
    fb_token = os.getenv('FB_TOKEN')
    tg_token = os.getenv('TG_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    vk_token = os.getenv('VK_TOKEN')
    vk_group_id = os.getenv('VK_GROUP_ID')

    fb.post_image_and_text(photos_path, text, fb_token, fb_group_id)
    tg.post_image_and_text(photos_path, text, tg_token, tg_chat_id)
    vk.post_image_and_text(photos_path, text, vk_token, vk_group_id)


if __name__ == '__main__':
    main()
