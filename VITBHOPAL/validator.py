# validator.py
# Functions that check the input given by the user

import math
from currencies import currencies


def is_valid_currency(code):
    """True if the code is present in our currency list"""
    return code in currencies


def get_valid_amount(text):
    """
    Converts the text to a number.
    Returns the number if it is valid, otherwise returns None.
    """
    try:
        amount = float(text)
    except ValueError:
        return None

    # float("nan") and float("inf") also pass float(), so check them
    if not math.isfinite(amount):
        return None

    if amount < 0:
        return None

    return amount


def clean_code(text):
    """Removes spaces and makes the code uppercase"""
    return text.strip().upper()
