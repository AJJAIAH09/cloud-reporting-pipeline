from validation.validator import DataValidator


def test_valid_user():

    validator = DataValidator()

    users = [
        {
            "id": 1,
            "name": "Ramesh",
            "email": "ramesh@test.com"
        }
    ]

    result = validator.validate_users(
        users
    )

    assert len(result) == 1


def test_invalid_user():

    validator = DataValidator()

    users = [
        {
            "id": 1,
            "name": "Ramesh"
        }
    ]

    result = validator.validate_users(
        users
    )

    assert len(result) == 0
