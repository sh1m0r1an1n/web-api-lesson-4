import requests


def main():
    response = requests.get(
        "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    )
    response.raise_for_status()
    with open("hubble.jpeg", "wb") as file:
        file.write(response.content)


if __name__ == "__main__":
    main()
