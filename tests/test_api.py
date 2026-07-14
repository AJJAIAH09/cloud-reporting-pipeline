from api.api_client import APIClient


def test_api_client_creation():

    client = APIClient(
        "https://test.com"
    )

    assert (
        client.base_url
        ==
        "https://test.com"
    )

