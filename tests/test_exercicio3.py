import pytest
from exercicios.exercicio3 import validate_email


def test_valid_email():
    assert validate_email("user123-u_ser@domain123.com") is None


def test_invalid_username_raise_exception():
    with pytest.raises(ValueError):
        validate_email("us%er@domain.com")


def test_username_when_doesnt_start_with_letter_raise_exception():
    with pytest.raises(ValueError):
        validate_email("1@domain.com")


def test_invalid_domain_raise_exception():
    with pytest.raises(ValueError):
        validate_email("user@domain_123.com")


def test_invalid_extension_raise_exception():
    with pytest.raises(ValueError):
        validate_email("user@domain.coms")
