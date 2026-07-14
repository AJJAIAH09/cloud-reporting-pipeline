import subprocess


class TerraformRunner:

    def __init__(
        self,
        terraform_dir="terraform"
    ):
        self.terraform_dir = terraform_dir

    def run_command(
        self,
        command
    ):

        result = subprocess.run(
            command,
            cwd=self.terraform_dir,
            capture_output=True,
            text=True,
            shell=True
        )

        print(result.stdout)

        if result.returncode != 0:
            print(result.stderr)

        return result.returncode

    def terraform_init(self):

        return self.run_command(
            "terraform init"
        )

    def terraform_plan(self):

        return self.run_command(
            "terraform plan"
        )
