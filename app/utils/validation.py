import re

def validate_email(email):
    if not email:
        return False
    regex = r"[^@]+@[^@]+\.[^@]+"
    return re.match(regex, email) is not None

def validate_phone_number(phone_number):
    if not phone_number:
        return False
    regex = r"^[0-9]{10}$"
    return re.match(regex, phone_number) is not None
