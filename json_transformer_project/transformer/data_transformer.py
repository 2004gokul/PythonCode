import datetime
import re
from dateutil import parser

def transform_user(user):
    try:
        full_name = f"{user['first_name']} {user['last_name']}"
        phone_match = re.match(r"\+(\d+)-(\d+)", user['phone'])

        age = datetime.date.today().year - parser.parse(user['dob']).year
        is_adult = age >= 18

        address_parts = user['address'].split(',')
        city, country = address_parts[-2].strip(), address_parts[-1].strip()

        return {
            "name": full_name,
            "email": user["email"],
            "country_code": phone_match.group(1),
            "phone_number": phone_match.group(2),
            "age": age,
            "is_adult": is_adult,
            "location": {
                "full_address": user["address"],
                "city": city,
                "country": country
            },
            "last_login_ts": int(parser.parse(user["last_login"]).timestamp()),
            "language_main": user["language"].split('-')[0],
            "contact_preference": user["preferred_contact"].lower(),
            "social_links": {
                "linkedin": user["social"]["linkedin"],
                "twitter": f"https://twitter.com/{user['social']['twitter'].lstrip('@')}"
            },
            "status_code": 1 if user["subscription_status"] == "Active" else 0
        }
    except Exception as e:
        from utils.logger import logger
        logger.error(f"Transformation error: {e}")
        return None
