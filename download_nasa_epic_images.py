import os
import json
from dotenv import load_dotenv
from datetime import datetime
from send_get_request import send_get_request
from download_image import download_image


def download_nasa_epic_images():
    directory = "NASA_EPIC"
    os.makedirs(directory, exist_ok=True)

    load_dotenv()
    nasa_api = os.environ["NASA_API"]

    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": nasa_api,
    }

    response = send_get_request(url, params)

    data_list = response.json()
    base_url = "https://api.nasa.gov/EPIC/archive/natural"
    image_urls = []

    for data in data_list:
        date_str = data["date"]
        image_name = data["image"]

        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        year, month, day = dt.strftime("%Y"), dt.strftime("%m"), dt.strftime("%d")

        image_urls.append(
            f"{base_url}/{year}/{month}/{day}/png/{image_name}.png?api_key={nasa_api}"
        )

    file_name = f"{directory}.json"  # Удалить после теста
    file_path = os.path.join(directory, file_name)  # Удалить после теста
    with open(file_path, "w") as file:  # Удалить после теста
        json.dump(response.json(), file)  # Удалить после теста

    download_image(image_urls, directory)


if __name__ == "__main__":
    download_nasa_epic_images()
