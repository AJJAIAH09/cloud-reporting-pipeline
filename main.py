from config.settings import Settings
from config.logger import setup_logger

from api.api_client import APIClient

from validation.validator import (
    DataValidator
)

from reports.report_generator import (
    ReportGenerator
)
from notifications.email_sender import (
    EmailSender
)
from infra.terraform_runner import (
    TerraformRunner
)
logger = setup_logger()


def main():
    terraform = TerraformRunner()

    logger.info(
        "Running Terraform Init"
    )

    terraform.terraform_init()

    logger.info(
        "Running Terraform Plan"
    )

    terraform.terraform_plan()
    logger.info(
        "Pipeline Started"
    )

    client = APIClient(
        Settings.API_BASE_URL
    )

    users = client.get_users()

    logger.info(
        f"Retrieved "
        f"{len(users)} users"
    )

    validator = DataValidator()

    valid_users = (
        validator.validate_users(users)
    )

    logger.info(
        f"Valid users: "
        f"{len(valid_users)}"
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

    logger.info(
        "Reports Generated"
    )
    email_sender = EmailSender(
        Settings.SMTP_SERVER,
        Settings.SMTP_PORT,
        Settings.SMTP_USER,
        Settings.SMTP_PASSWORD
    )

    email_sender.send_email(
        Settings.EMAIL_TO,
        "Daily Pipeline Report",
        (
            "Pipeline executed "
            "successfully."
        )
    )

    logger.info(
        "Pipeline Completed"
    )


if __name__ == "__main__":
    main()
