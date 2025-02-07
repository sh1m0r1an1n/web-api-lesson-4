import os
import random
import time
import requests
import configargparse
from environs import Env
import telegram


def generate_image_paths(directory):
    image_paths = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(
                    (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp")
            ):
                image_paths.append(os.path.join(root, file))
    return image_paths


def send_images_without_ending(bot, channel_id, image_paths, seconds):
    while True:
        for image_path in image_paths:
            try:
                with open(image_path, "rb") as photo:
                    bot.send_photo(chat_id=channel_id, photo=photo)
            except telegram.error.NetworkError as error:
                print(f"Ошибка сети при отправке {image_path}: {error}")
                time.sleep(5)
                continue
            except Exception as error:
                print(f"Неожиданная ошибка при отправке {image_path}: {error}")
                time.sleep(5)
                continue
            time.sleep(seconds)
        random.shuffle(image_paths)


def filter_files_by_size(image_paths):
    max_file_size_mb = 20
    max_file_size_bytes = max_file_size_mb * 1024 * 1024
    image_paths = [image_path for image_path in image_paths if os.path.getsize(image_path) < max_file_size_bytes]
    return image_paths


def launch_telegram_bot(env, hours, bot_token, channel_id, directory):
    seconds = hours  * 60  * 60

    bot = telegram.Bot(bot_token)

    image_paths = generate_image_paths(directory)
    random.shuffle(image_paths)

    image_paths = filter_files_by_size(image_paths)
    send_images_without_ending(bot, channel_id, image_paths, seconds)


if __name__ == "__main__":
    env = Env()
    env.read_env()

    bot_token = env.str("TG_BOT_TOKEN")
    channel_id = env.str("TG_CHANNEL_ID")

    parser = configargparse.ArgumentParser(
        default_config_file=['config.ini'],
        description="Программа запускает бота для публикации фото из директорий проекта в телеграм канал."
    )
    parser.add_argument(
        "--hours", type=int, help="Время задержки между постами, в часах", default=4
    )
    parser.add_argument("--directory", type=str, help="Директория, откуда бот будет брать фото для отправки.",
                        default="images")

    hours = parser.parse_args().hours
    directory = parser.parse_args().directory

    try:
        launch_telegram_bot(env, hours, bot_token, channel_id, directory)
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при выполнении запроса: {error}")
