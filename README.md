Processing user data stored as JSON files. The data is "semi-clean" and inconsistently structured. Your job is to normalize, transform, enrich, and store the cleaned data in a structured format.


output_writer/local_writer.py
Writes transformed data to .json files with _transformed suffix.
Ensures output path is valid and writable.


Sample input JSON:
{
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


Sample output json:
{
  "name": "Alice Johnson",
  "email": "alice.j@example.com",
  "country_code": "91",
  "phone_number": "9876543210",
  "age": 29,
  "is_adult": true,
  "location": {
    "full_address": "56 Residency Road, Bangalore, India",
    "city": "Bangalore",
    "country": "India"
  },
  "last_login_ts": 1752460200,
  "language_main": "en",
  "contact_preference": "email",
  "social_links": {
    "linkedin": "https://linkedin.com/in/alicejohnson",
    "twitter": "https://twitter.com/alice_j"
  },
  "status_code": 1
}




