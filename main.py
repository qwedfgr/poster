import os

from dotenv import load_dotenv

import fb
import tg
import vk


def main():
    load_dotenv()
    photos_path = os.getenv('PHOTOS_PATH')
    text = os.getenv('TEXT')
    fb.post_image_and_text(photos_path, text)
    tg.post_image_and_text(photos_path, text)
    vk.post_image_and_text(photos_path, text)


if __name__ == '__main__':
    main()
