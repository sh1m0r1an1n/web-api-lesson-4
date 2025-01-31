import requests
import os


def download_picture(url, file_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при загрузке изображения: {error}")
        return

    with open(file_path, "wb") as file:
        file.write(response.content)


def main():
    directory = "images"
    file_name = "hubble.jpeg"
    file_path = os.path.join(directory, file_name)

    os.makedirs(directory, exist_ok=True)
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    download_picture(url, file_path)


if __name__ == "__main__":
    main()
