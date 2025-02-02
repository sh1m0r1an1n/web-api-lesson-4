import os
import random
import time
import argparse
from environs import Env
import telegram


def launch_telegram_bot():
    parser = argparse.ArgumentParser(
        description="Программа запускает бота для публикации фото из директорий проекта в телеграм канал."
    )
    parser.add_argument(
        "--hours", type=int, help="Время задержки между постами, в часах", default=5
    )
    hours = parser.parse_args().hours

    env = Env()
    env.read_env()

    hours = env.int("DELAY_HOURS", default=hours)
    seconds = hours  * 60  * 60

    bot_token = env.str("TG_BOT_API")
    bot = telegram.Bot(bot_token)
    channel_id = env.str("TG_CHANNEL_ID")

    directories = ["NASA_APOD", "NASA_EPIC", "SpaceX"]
    image_paths = []

    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(
                    (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp")
                ):
                    image_paths.append(os.path.join(root, file))

    random.shuffle(image_paths)

    MAX_FILE_SIZE_MB = 20
    MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

    while True:
        for image_path in image_paths:
            if os.path.getsize(image_path) < MAX_FILE_SIZE_BYTES:
                with open(image_path, "rb") as photo:
                    bot.send_photo(chat_id=channel_id, photo=photo)
                    time.sleep(seconds)
        random.shuffle(image_paths)


if __name__ == "__main__":
    launch_telegram_bot()
