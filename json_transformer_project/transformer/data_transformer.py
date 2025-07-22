from datetime import datetime, date
import re

def calculate_age(dob_str):
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return 0
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

def extract_country_code_and_number(phone_str):
    phone_digits = re.sub(r'\D', '', phone_str)
    if len(phone_digits) > 10:
        country_code = phone_digits[:-10]
    else:
        country_code = ''
    phone_number = phone_digits[-10:] if len(phone_digits) >= 10 else ''
    return country_code, phone_number

def normalize_address(address):
    if not isinstance(address, str):
        return ''
    cleaned = address.strip().replace('\n', ', ')
    return re.sub(r'\s{2,}', ' ', cleaned)

def transform_user(user_data):
    first = user_data.get('first_name', '').strip()
    last = user_data.get('last_name', '').strip()
    name = f"{first} {last}".strip()

    phone = user_data.get("phone", "")
    country_code, phone_number = extract_country_code_and_number(phone)

    age = calculate_age(user_data.get("dob", "1900-01-01"))

    transformed = {
        "name": name,
        "country_code": country_code,
        "phone_number": phone_number,
        "age": age,
        "is_adult": age >= 18,
        "email": user_data.get("email", "").strip(),
        "address": normalize_address(user_data.get("address", "")),
        "status": user_data.get("subscription_status", "").strip().lower(),
        "last_login": user_data.get("last_login", ""),
        "preferred_contact": user_data.get("preferred_contact", "").strip().lower(),
        "language": user_data.get("language", "").strip().lower(),
        "social": user_data.get("social", {}) if isinstance(user_data.get("social"), dict) else {}
    }

    return transformed
