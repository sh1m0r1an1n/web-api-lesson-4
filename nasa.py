import os
import json
from urllib.parse import urlparse
from dotenv import load_dotenv
from api_request import api_request


def picture_extension(url):
    path = urlparse(url).path
    filename = os.path.basename(path)
    name, extension = os.path.splitext(filename)
    return extension


def nasa():
    directory = "nasa"
    os.makedirs(directory, exist_ok=True)

    load_dotenv()
    token = os.environ["NASA_API"]

    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": token,
        "count": 50,
    }

    response = api_request(url, params)

    image_urls = [i["url"] for i in response.json() if "url" in i]

    file_name = "response.json"
    file_path = os.path.join(directory, file_name)
    with open(file_path, "w") as file:
        json.dump(response.json(), file)

    for i, image_url in enumerate(image_urls, start=1):
        extension = picture_extension(image_url)
        file_name = f"nasa_{i}.{extension}"
        file_path = os.path.join(directory, file_name)
        response = api_request(image_url)
        with open(file_path, "wb") as file:
            file.write(response.content)


if __name__ == "__main__":
    nasa()
