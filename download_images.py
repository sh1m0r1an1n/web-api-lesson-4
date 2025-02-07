import os
from urllib.parse import urlparse

from send_get_request import send_get_request


def get_image_extension(image_url):
    path = urlparse(image_url).path
    filename = os.path.basename(path)
    _, extension = os.path.splitext(filename)
    return extension


def generate_file_path(directory, index, image_url):
    extension = get_image_extension(image_url)
    file_name = f"{directory}_{index}{extension}"
    return os.path.join(directory, file_name)


def download_single_image(image_url, file_path):
    response = send_get_request(image_url)
    if hasattr(response, "content"):
        with open(file_path, "wb") as file:
            file.write(response.content)


def download_images(image_urls, directory):
    for index, image_url in enumerate(image_urls, start=1):
        file_path = generate_file_path(directory, index, image_url)
        download_single_image(image_url, file_path)



