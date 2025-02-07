import os
import requests
import configargparse

from send_get_request import send_get_request
from download_images import download_images


def spacex_launch_get_request(spacex_launch_id):
    url = f"https://api.spacexdata.com/v5/launches/{spacex_launch_id}"
    response = send_get_request(url)
    image_urls = response.json()["links"]["flickr"]["original"]
    return image_urls


def download_spacex_launch_images(spacex_launch_id, directory):
    file_name = "SpaceX"
    os.makedirs(directory, exist_ok=True)

    image_urls = spacex_launch_get_request(spacex_launch_id)
    download_images(image_urls, directory, file_name)


if __name__ == "__main__":
    parser = configargparse.ArgumentParser(
        description="Программа скачивает фото запуска SpaceX по его id,"
            "по умолчанию крайний запуск.",
        default_config_files=['config.ini']
    )
    parser.add_argument(
        "--id", type=str, help="id запуска SpaceX", default="latest"
    )
    parser.add_argument(
        "--directory", type=str,
        help="Директория, куда будут скачиваться фотографии.",
        default="images"
    )
    args, unknown_args = parser.parse_known_args()
    spacex_launch_id = args.id
    directory = args.directory

    try:
        download_spacex_launch_images(spacex_launch_id, directory)
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при выполнении запроса: {error}")
