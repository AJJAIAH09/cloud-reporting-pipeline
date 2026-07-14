class DataValidator:

    REQUIRED_FIELDS = [
        "id",
        "name",
        "email"
    ]

    def validate_users(self, users):

        valid_users = []

        for user in users:

            is_valid = True

            for field in self.REQUIRED_FIELDS:

                if (
                    field not in user
                    or not user[field]
                ):
                    print(
                        f"Validation Failed: "
                        f"{field} missing"
                    )

                    is_valid = False
                    break

            if is_valid:
                valid_users.append(user)

        return valid_users
