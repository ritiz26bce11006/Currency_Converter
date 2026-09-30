# currencies.py
# Currency data and the functions related to showing / searching it

# code: (name, symbol)
# NOTE: only the currencies supported by the Frankfurter API are kept here
currencies = {
    "AUD": ("Australian Dollar", "A$"),
    "BRL": ("Brazilian Real", "R$"),
    "CAD": ("Canadian Dollar", "C$"),
    "CHF": ("Swiss Franc", "CHF"),
    "CNY": ("Chinese Yuan", "¥"),
    "CZK": ("Czech Koruna", "Kč"),
    "DKK": ("Danish Krone", "kr"),
    "EUR": ("Euro", "€"),
    "GBP": ("British Pound", "£"),
    "HKD": ("Hong Kong Dollar", "HK$"),
    "HUF": ("Hungarian Forint", "Ft"),
    "IDR": ("Indonesian Rupiah", "Rp"),
    "ILS": ("Israeli New Shekel", "₪"),
    "INR": ("Indian Rupee", "₹"),
    "ISK": ("Icelandic Krona", "kr"),
    "JPY": ("Japanese Yen", "¥"),
    "KRW": ("South Korean Won", "₩"),
    "MXN": ("Mexican Peso", "$"),
    "MYR": ("Malaysian Ringgit", "RM"),
    "NOK": ("Norwegian Krone", "kr"),
    "NZD": ("New Zealand Dollar", "NZ$"),
    "PHP": ("Philippine Peso", "₱"),
    "PLN": ("Polish Zloty", "zł"),
    "RON": ("Romanian Leu", "lei"),
    "SEK": ("Swedish Krona", "kr"),
    "SGD": ("Singapore Dollar", "S$"),
    "THB": ("Thai Baht", "฿"),
    "TRY": ("Turkish Lira", "₺"),
    "USD": ("US Dollar", "$"),
    "ZAR": ("South African Rand", "R"),
}


def show_currencies():
    """Prints all the currencies, one blank line after every 4"""
    print("\nCURRENCY LIST")

    count = 0
    for code, (name, symbol) in currencies.items():
        print(f"{code} - {name} ({symbol})")
        count += 1
        if count % 4 == 0:
            print()

    print("\nTotal currencies listed:", len(currencies))


def search_currency(text):
    """Returns a list of codes whose code or name contains the text"""
    text = text.lower().strip()
    found = []

    for code, (name, symbol) in currencies.items():
        if text in code.lower() or text in name.lower():
            found.append(code)

    return found


def get_name(code):
    """Returns the full name of a currency code"""
    return currencies[code][0]
