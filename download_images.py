import os
from urllib.parse import urlparse

from send_get_request import send_get_request


def get_image_extension(image_url):
    path = urlparse(image_url).path
    filename = os.path.basename(path)
    _, extension = os.path.splitext(filename)
    return extension


def download_images(image_urls, directory):
    for i, image_url in enumerate(image_urls, start=1):
        extension = get_image_extension(image_url)
        file_name = f"{directory}_{i}{extension}"
        file_path = os.path.join(directory, file_name)
        response = send_get_request(image_url)
        with open(file_path, "wb") as file:
            if hasattr(response, "content"):
                file.write(response.content)
