from exercicios.exercicio3 import validate_email


def get_valid_emails(email_list: list[str]) -> list[str]:
    valid_emails = []
    for email in email_list:
        try:
            validate_email(email)
            valid_emails.append(email)
        except ValueError:
            print(f"{email} is not a valid email")

    return valid_emails
