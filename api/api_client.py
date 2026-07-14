import json
import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_users(self):

        response = requests.get(self.base_url)

        response.raise_for_status()

        return response.json()

    def save_users(self, users, filepath):

        with open(filepath, "w") as file:
            json.dump(
                users,
                file,
                indent=4
            )

        print(
            f"Data saved successfully: {filepath}"
        )
