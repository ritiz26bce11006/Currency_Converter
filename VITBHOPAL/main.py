# main.py
# Starting point of the World Currency Converter

from currency_converter import convert_currency
from currencies import show_currencies, search_currency, get_name
from history_manager import show_history, clear_history
from logger_setup import setup_logger

logger = setup_logger()


def search_menu():
    text = input("Enter currency name or code to search: ")
    results = search_currency(text)

    if not results:
        print("No currency found.")
        return

    for code in results:
        print(f"{code} - {get_name(code)}")


def main():
    logger.info("Program started")

    while True:
        print("\n")
        print("       WORLD CURRENCY CONVERTER")
        print("1. Convert Currency")
        print("2. Show Currency List")
        print("3. Search Currency")
        print("4. Conversion History")
        print("5. Clear History")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            convert_currency()
        elif choice == "2":
            show_currencies()
        elif choice == "3":
            search_menu()
        elif choice == "4":
            show_history()
        elif choice == "5":
            clear_history()
        elif choice == "6":
            print("\nThank you for using World Currency Converter!")
            logger.info("Program closed")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
