import os
import argparse

from send_get_request import send_get_request
from download_images import download_images


def download_spacex_launch_images(id_spacex_launch):
    directory = "SpaceX"
    os.makedirs(directory, exist_ok=True)
    url = f"https://api.spacexdata.com/v5/launches/{id_spacex_launch}"

    response = send_get_request(url)

    image_urls = response.json()["links"]["flickr"]["original"]

    download_images(image_urls, directory)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Программа скачивает фото запуска SpaceX по его id, по умолчанию крайний запуск."
    )
    parser.add_argument("--id", type=str, help="id запуска SpaceX", default="latest")
    id_spacex_launch = parser.parse_args().id

    download_spacex_launch_images(id_spacex_launch)
