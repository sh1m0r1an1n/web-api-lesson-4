import os
import argparse
from api_request import api_request


def fetch_spacex_last_launch():
    parser = argparse.ArgumentParser(
        description="Программа скачивает фото запуска SpaceX по его id."
    )
    parser.add_argument("--id", type=str, help="id запуска SpaceX", default="latest")
    id = parser.parse_args().id

    directory = "spacex"
    os.makedirs(directory, exist_ok=True)
    url = f"https://api.spacexdata.com/v5/launches/{id}"

    response = api_request(url)

    image_urls = response.json()["links"]["flickr"]["original"]

    for i, image_url in enumerate(image_urls, start=1):
        file_name = f"spacex_{i}.jpg"
        file_path = os.path.join(directory, file_name)
        response = api_request(image_url)
        with open(file_path, "wb") as file:
            file.write(response.content)


if __name__ == "__main__":
    fetch_spacex_last_launch()
