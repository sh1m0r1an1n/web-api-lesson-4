import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv


def fetch_spacex_last_launch():
    directory = "images"
    os.makedirs(directory, exist_ok=True)
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при получении данных: {error}")
        return
    except ValueError:
        print("Ошибка при декодировании JSON.")
        return

    image_urls = response.json()["links"]["flickr"]["original"]

    if not image_urls:
        print("Изображения не найдены.")
        return

    for i, image_url in enumerate(image_urls, start=1):
        file_name = f"spacex_{i}.jpg"
        file_path = os.path.join(directory, file_name)
        try:
            response = requests.get(image_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            print(f"Ошибка при загрузке изображения {image_url}: {error}")
            return
        with open(file_path, "wb") as file:
            file.write(response.content)


def picture_extension(url):
    path = urlparse(url).path
    filename = os.path.basename(path)
    name, extension = os.path.splitext(filename)
    return name, extension


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

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при получении данных: {error}")
        return
    except ValueError:
        print("Ошибка при декодировании JSON.")
        return

    image_urls = [i["url"] for i in response.json()]

    for i, image_url in enumerate(image_urls, start=1):
        name, extension = picture_extension(image_url)
        file_name = f"nasa_{i}.{extension}"
        file_path = os.path.join(directory, file_name)
        try:
            response = requests.get(image_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            print(f"Ошибка при загрузке изображения {image_url}: {error}")
            return
        with open(file_path, "wb") as file:
            file.write(response.content)


def epic():
    directory = "epic"
    os.makedirs(directory, exist_ok=True)

    load_dotenv()
    token = os.environ["NASA_API"]

    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": token,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при получении данных: {error}")
        return
    except ValueError:
        print("Ошибка при декодировании JSON.")
        return

    data_list = response.json()
    base_url = "https://api.nasa.gov/EPIC/archive/natural"
    image_urls = []

    for data in data_list:
        date_str = data["date"]  # "2025-01-30 00:03:42"
        image_name = data["image"]  # "epic_1b_20250130000830"

        date_parts = date_str.split()[0].split("-")
        year, month, day = date_parts

        image_urls.append(
            f"{base_url}/{year}/{month}/{day}/png/{image_name}.png?api_key={token}"
        )

    for i, image_url in enumerate(image_urls, start=1):
        file_name = f"epic_{i}.png"
        file_path = os.path.join(directory, file_name)
        try:
            response = requests.get(image_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            print(f"Ошибка при загрузке изображения {image_url}: {error}")
            return
        with open(file_path, "wb") as file:
            file.write(response.content)


def main():
    # fetch_spacex_last_launch()
    url = "https://apod.nasa.gov/apod/image/2501/HubblesVariablecopy1024.jpg"
    # picture_extension(url)
    epic()


if __name__ == "__main__":
    main()
