from datetime import datetime, date
from transformer.data_transformer import transform_user

def test_transformation():
    sample_input = {
        "first_name": "Alice",
        "last_name": "Johnson",
        "phone": "+91-9876543210",
        "dob": "1995-08-15",
        "email": "alice.j@example.com",
        "address": "56 Residency Road, Bangalore, India",
        "subscription_status": "Active",
        "last_login": "2025-07-10T18:30:00",
        "preferred_contact": "email",
        "social": {
            "linkedin": "https://linkedin.com/in/alicejohnson",
            "twitter": "@alice_j"
        },
        "language": "en-IN"
    }

    transformed = transform_user(sample_input)

    # Check names and phones
    assert transformed["name"] == "Alice Johnson"
    assert transformed["country_code"] == "91"
    assert transformed["phone_number"] == "9876543210"

    # Calculate expected age dynamically for test reliability
    dob = datetime.strptime(sample_input["dob"], "%Y-%m-%d").date()
    today = date.today()
    expected_age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    assert transformed["age"] == expected_age

    # Other asserts
    assert transformed["is_adult"] is (expected_age >= 18)
    assert transformed["status"] == "active"
