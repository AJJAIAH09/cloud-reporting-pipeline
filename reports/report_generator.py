import pandas as pd

from jinja2 import (
    Environment,
    FileSystemLoader
)


class ReportGenerator:

    def generate_csv(
        self,
        users,
        output_file
    ):

        df = pd.DataFrame(users)

        df.to_csv(
            output_file,
            index=False
        )

        print(
            f"CSV Report Generated: "
            f"{output_file}"
        )

    def generate_html(
        self,
        users,
        output_file
    ):

        env = Environment(
            loader=FileSystemLoader(
                "reports/templates"
            )
        )

        template = env.get_template(
            "report.html"
        )

        html_content = template.render(
            users=users,
            total_users=len(users)
        )

        with open(
            output_file,
            "w"
        ) as file:

            file.write(html_content)

        print(
            f"HTML Report Generated: "
            f"{output_file}"
        )
