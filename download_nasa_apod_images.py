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


def download_nasa_apod_images(directory, response):
    os.makedirs(directory, exist_ok=True)

    file_name = "nasa_apod"
    image_urls = [i["url"] for i in response
                  if "url" in i and i["media_type"] == "image"]
    download_images(image_urls, directory, file_name)


def main():
    env = Env()
    env.read_env()

    nasa_api = env.str("NASA_API_TOKEN")

    parser = configargparse.ArgumentParser(
        description="Передайте необходимые аргументы.",
        default_config_files=['config.ini']
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

    args, unknown_args = parser.parse_known_args()
    directory = args.directory
    count = args.count

    try:
        response = send_nasa_apod_get_request(nasa_api, count)
        download_nasa_apod_images(directory, response)
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при выполнении запроса: {error}")


if __name__ == "__main__":
    main()
