import os
import argparse

from send_get_request import send_get_request
from download_image import download_image


def download_spacex_launch_images():
    parser = argparse.ArgumentParser(
        description="Программа скачивает фото запуска SpaceX по его id, по умолчанию крайний запуск."
    )
    parser.add_argument("--id", type=str, help="id запуска SpaceX", default="latest")
    id_spacex_launch = parser.parse_args().id

    directory = "SpaceX"
    os.makedirs(directory, exist_ok=True)
    url = f"https://api.spacexdata.com/v5/launches/{id_spacex_launch}"

    response = send_get_request(url)

    image_urls = response.json()["links"]["flickr"]["original"]

    download_image(image_urls, directory)


if __name__ == "__main__":
    download_spacex_launch_images()
