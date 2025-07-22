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
    assert transformed["name"] == "Alice Johnson"
    assert transformed["country_code"] == "91"
    assert transformed["phone_number"] == "9876543210"
    assert transformed["is_adult"] == True
    assert transformed["location"]["city"] == "Bangalore"
    assert transformed["status_code"] == 1
