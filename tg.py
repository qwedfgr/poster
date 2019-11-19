import telegram


def post_image_and_text(image_path, text, token, chat_id):
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=chat_id, text=text)
    with open(image_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo, text=text)
