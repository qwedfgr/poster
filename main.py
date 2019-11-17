from dotenv import load_dotenv

import fb
import tg
import vk


def main():
    load_dotenv()
    photos_path = 'images/2.jpg'
    text = 'Привет'
    fb.post_image_and_text(photos_path, text)
    tg.post_image_and_text(photos_path, text)
    vk.post_image_and_text(photos_path, text)


if __name__ == '__main__':
    main()
