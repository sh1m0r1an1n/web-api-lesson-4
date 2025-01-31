import os
from dotenv import load_dotenv
from api_request import api_request


def epic():
    directory = "epic"
    os.makedirs(directory, exist_ok=True)

    load_dotenv()
    token = os.environ["NASA_API"]

    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        "api_key": token,
    }

    response = api_request(url, params)

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
        response = api_request(image_url)
        with open(file_path, "wb") as file:
            file.write(response.content)


if __name__ == "__main__":
    epic()
