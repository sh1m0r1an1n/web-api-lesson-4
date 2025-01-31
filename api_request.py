import requests


def api_request(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при выполнении запроса: {error}")
        return None
    except ValueError:
        print("Ошибка при декодировании JSON.")
        return None
