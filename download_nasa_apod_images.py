import os
import json
from dotenv import load_dotenv
from send_get_request import send_get_request
from download_image import download_image


def download_nasa_apod_images():
    directory = "NASA_APOD"
    os.makedirs(directory, exist_ok=True)

    load_dotenv()
    nasa_api = os.environ["NASA_API"]

    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": nasa_api,
        "count": 100,
    }

    response = send_get_request(url, params)

    image_urls = [i["url"] for i in response.json() if "url" in i]

    file_name = f"{directory}.json"  # Удалить после теста
    file_path = os.path.join(directory, file_name)  # Удалить после теста
    with open(file_path, "w") as file:  # Удалить после теста
        json.dump(response.json(), file)  # Удалить после теста

    download_image(image_urls, directory)


if __name__ == "__main__":
    download_nasa_apod_images()
