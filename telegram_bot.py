import os
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.environ["TG_API"]
    bot = telegram.Bot(token)
    updates = bot.get_updates()

    print(bot.get_me())
    updates = bot.get_updates()

    chat_id = updates[0].message.from_user.id
    bot.send_message(text="Hi John!", chat_id=chat_id)

    chat_id = "@Galaxy_Gallery_Url"
    bot.send_message(chat_id=chat_id, text="Hello.")


if __name__ == "__main__":
    main()
