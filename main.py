import requests
import os


def download_picture(url, file_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при загрузке изображения {url}: {error}")
        return

    with open(file_path, "wb") as file:
        file.write(response.content)


def main():
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
        download_picture(image_url, file_path)


if __name__ == "__main__":
    main()
