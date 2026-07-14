from config.settings import Settings
from api.api_client import APIClient
from validation.validator import DataValidator
from reports.report_generator import (
    ReportGenerator
)


def main():

    print("\nStarting API Pipeline")
    print("-" * 50)

    client = APIClient(
        Settings.API_BASE_URL
    )

    users = client.get_users()

    print(
        f"Retrieved Users : {len(users)}"
    )

    validator = DataValidator()

    valid_users = (
        validator.validate_users(users)
    )

    print(
        f"Valid Users     : {len(valid_users)}"
    )

    client.save_users(
        valid_users,
        "data/raw/users.json"
    )

    report = ReportGenerator()

    report.generate_csv(
        valid_users,
        "data/processed/users.csv"
    )
    report.generate_html(
        valid_users,
        "data/processed/users.html"
    )
    print(
        "\nReporting completed."
    )


if __name__ == "__main__":
    main()

