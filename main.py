from config.settings import Settings


def main():

    print("\nConfiguration Test")
    print("-" * 40)

    print(
        f"Azure Resource Group : {Settings.AZURE_RESOURCE_GROUP}"
    )

    print(
        f"Azure Location       : {Settings.AZURE_LOCATION}"
    )

    print(
        f"API URL              : {Settings.API_BASE_URL}"
    )

    print(
        f"SMTP Server          : {Settings.SMTP_SERVER}"
    )


if __name__ == "__main__":
    main()
