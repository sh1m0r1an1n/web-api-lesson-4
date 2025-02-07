import os
import requests
import configargparse
from environs import Env

from send_get_request import send_get_request
from download_images import download_images


def send_nasa_apod_get_request(nasa_api, count):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": nasa_api,
        "count": count
    }
    response = send_get_request(url, params)
    return response.json()


def download_nasa_apod_images(nasa_api, directory, count):
    os.makedirs(directory, exist_ok=True)

    file_name = "nasa_apod"
    response = send_nasa_apod_get_request(nasa_api, count)
    image_urls = [i["url"] for i in response if "url" in i and i["media_type"] == "image"]
    download_images(image_urls, directory, file_name)


if __name__ == "__main__":
    env = Env()
    env.read_env()

    nasa_api = env.str("NASA_API_TOKEN")

    parser = configargparse.ArgumentParser(
        default_config_file=['config.ini'],
        description="Передайте необходимые аргументы."
    )
    parser.add_argument(
        "--directory", type=str,
        help="Директория, куда будут скачиваться фотографии.",
        default="images"
    )
    parser.add_argument(
        "--count",
        type=int,
        help="Количество фотографий для скачивания.",
        default=100
    )

    directory = parser.parse_args().directory
    count = parser.parse_args().count

    try:
        download_nasa_apod_images(nasa_api, directory, count)
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при выполнении запроса: {error}")
