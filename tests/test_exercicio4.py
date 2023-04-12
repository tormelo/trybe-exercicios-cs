from exercicios.exercicio4 import get_valid_emails


def test_if_doesnt_have_emails_returns_empty_list():
    assert get_valid_emails([]) == []


def test_only_valid_emails():
    emails = ["username@website.com", "user@domain.net"]
    assert get_valid_emails(emails) == emails


def test_only_invalid_emails():
    emails = ["inv*alid@website.com", "1@domain.com"]
    assert get_valid_emails(emails) == []


def test_valid_and_invalid_emails_returns_only_valids():
    emails = ["user@domain.com", "invalid@dom!ain.com"]
    expected_emails = ["user@domain.com"]
    assert get_valid_emails(emails) == expected_emails
