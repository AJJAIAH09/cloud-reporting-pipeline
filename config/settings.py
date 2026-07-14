import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    AZURE_SUBSCRIPTION_ID = os.getenv(
        "AZURE_SUBSCRIPTION_ID"
    )

    AZURE_RESOURCE_GROUP = os.getenv(
        "AZURE_RESOURCE_GROUP"
    )

    AZURE_LOCATION = os.getenv(
        "AZURE_LOCATION"
    )

    API_BASE_URL = os.getenv(
        "API_BASE_URL"
    )

    API_TOKEN = os.getenv(
        "API_TOKEN"
    )

    SMTP_SERVER = os.getenv(
        "SMTP_SERVER"
    )

    SMTP_PORT = os.getenv(
        "SMTP_PORT"
    )

    SMTP_USER = os.getenv(
        "SMTP_USER"
    )

    SMTP_PASSWORD = os.getenv(
        "SMTP_PASSWORD"
    )

    EMAIL_TO = os.getenv(
        "EMAIL_TO"
    )
