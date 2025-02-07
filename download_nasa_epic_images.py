import os
from dotenv import load_dotenv
from datetime import datetime
from urllib.parse import urlparse, urlunparse, urlencode

from send_get_request import send_get_request
from download_images import download_images


def generate_image_urls_from_response_nasa_epic(data_list, nasa_api):
    base_url = "https://api.nasa.gov/EPIC/archive/natural"
    params = {"api_key": nasa_api}
    image_urls = []

    for data in data_list:
        date_str = data["date"]
        image_name = data["image"]

        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        year, month, day = dt.strftime("%Y"), dt.strftime("%m"), dt.strftime("%d")

        url = f"{base_url}/{year}/{month}/{day}/png/{image_name}.png"

        parsed_url = urlparse(url)
        query_string = urlencode(params)

        image_urls.append(
            urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, query_string, parsed_url.fragment))
        )
    return image_urls


def send_nasa_epic_get_request(nasa_api):
    url = "https://api.nasa.gov/EPIC/api/natural"
    params = {"api_key": nasa_api}
    response = send_get_request(url, params)
    return response.json()


def download_nasa_epic_images(nasa_api):
    directory = "NASA_EPIC"
    os.makedirs(directory, exist_ok=True)

    data_list = send_nasa_epic_get_request(nasa_api)
    image_urls = generate_image_urls_from_response_nasa_epic(data_list, nasa_api)
    download_images(image_urls, directory)


if __name__ == "__main__":
    load_dotenv()
    nasa_api = os.environ["NASA_API_TOKEN"]

    download_nasa_epic_images(nasa_api)
