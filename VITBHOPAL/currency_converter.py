# converter.py
# Main conversion feature

from currencies import get_name
from validator import is_valid_currency, get_valid_amount, clean_code
from api_handler import get_rate
from history_manager import add_record
from logger_setup import setup_logger

logger = setup_logger()


def calculate_result(amount, rate):
    """Multiplies the amount with the rate"""
    return amount * rate


def convert_currency():
    print("\nCURRENCY CONVERTER")

    from_currency = clean_code(input("Enter FROM currency code: "))
    to_currency = clean_code(input("Enter TO currency code: "))

    if not is_valid_currency(from_currency):
        print("Invalid FROM currency code.")
        return

    if not is_valid_currency(to_currency):
        print("Invalid TO currency code.")
        return

    amount = get_valid_amount(input("Enter amount: "))
    if amount is None:
        print("Please enter a valid positive number.")
        return

    # same currency -> no need to call the API
    if from_currency == to_currency:
        rate = 1.0
    else:
        rate = get_rate(from_currency, to_currency)
        if rate is None:
            print("Could not get the exchange rate. Check your internet and try again.")
            return

    result = calculate_result(amount, rate)

    print()
    print(f"{amount:.2f} {from_currency} ({get_name(from_currency)})")
    print(f"= {result:.2f} {to_currency} ({get_name(to_currency)})")
    print(f"Exchange Rate: 1 {from_currency} = {rate:.6f} {to_currency}")

    add_record(from_currency, to_currency, amount, result)
    logger.info(f"Converted {amount} {from_currency} to {result:.2f} {to_currency}")
