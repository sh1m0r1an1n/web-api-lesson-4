import os
import json
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

    file_name = f"{directory}.json"  # Удалить после теста
    file_path = os.path.join(directory, file_name)  # Удалить после теста
    with open(file_path, "w") as file:  # Удалить после теста
        json.dump(response.json(), file)  # Удалить после теста

    download_image(image_urls, directory)


if __name__ == "__main__":
    download_spacex_launch_images()
