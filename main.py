import requests
import os


def main():
    file_path = os.path.join("images", "hubble.jpeg")
    os.makedirs("images", exist_ok=True)

    response = requests.get(
        "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    )
    response.raise_for_status()

    with open(file_path, "wb") as file:
        file.write(response.content)


if __name__ == "__main__":
    main()
