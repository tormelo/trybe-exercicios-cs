import re


def validate_email(email):
    email_re = r"^[a-zA-Z][\w\-]{0,}@[a-zA-Z\d]+\.[a-zA-Z]{3}$"
    if not re.findall(email_re, email):
        raise ValueError("Invalid email")
