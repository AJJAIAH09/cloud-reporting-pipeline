import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:

    def __init__(
        self,
        smtp_server,
        smtp_port,
        smtp_user,
        smtp_password
    ):

        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(
        self,
        recipient,
        subject,
        message
    ):

        if (
            not self.smtp_user
            or not self.smtp_password
            or not recipient
        ):

            print(
                "SMTP configuration not provided."
            )

            print(
                "Skipping email step."
            )

            return

        email = MIMEMultipart()

        email["From"] = self.smtp_user
        email["To"] = recipient
        email["Subject"] = subject

        email.attach(
            MIMEText(
                message,
                "plain"
            )
        )

        with smtplib.SMTP(
            self.smtp_server,
            int(self.smtp_port)
        ) as server:

            server.starttls()

            server.login(
                self.smtp_user,
                self.smtp_password
            )

            server.send_message(email)

        print(
            "Email sent successfully."
        )
