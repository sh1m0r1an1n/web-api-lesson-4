import os
from dotenv import load_dotenv

from send_get_request import send_get_request
from download_images import download_images


def send_nasa_apod_get_request(nasa_api):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": nasa_api,
        "count": 100
    }
    response = send_get_request(url, params)
    return response.json()


def download_nasa_apod_images(nasa_api):
    directory = "images"
    os.makedirs(directory, exist_ok=True)

    file_name = "nasa_apod"
    response = send_nasa_apod_get_request(nasa_api)
    image_urls = [i["url"] for i in response if "url" in i and i["media_type"] == "image"]
    download_images(image_urls, directory, file_name)


if __name__ == "__main__":
    load_dotenv()
    nasa_api = os.environ["NASA_API_TOKEN"]

    download_nasa_apod_images(nasa_api)
