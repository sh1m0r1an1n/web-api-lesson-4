import os
from dotenv import load_dotenv

from send_get_request import send_get_request
from download_images import download_images


def download_nasa_apod_images(nasa_api):
    directory = "NASA_APOD"
    os.makedirs(directory, exist_ok=True)

    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": nasa_api,
        "count": 100,
    }

    response = send_get_request(url, params)

    image_urls = [i["url"] for i in response.json() if "url" in i and i["media_type"] == "image"]

    download_images(image_urls, directory)


if __name__ == "__main__":
    load_dotenv()
    nasa_api = os.environ["NASA_API"]

    download_nasa_apod_images(nasa_api)
