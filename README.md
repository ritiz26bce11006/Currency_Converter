# Currency Converter

## Overview
Currency Converter is a console-based Python application that converts money from one currency to another using live exchange rates from the [Frankfurter API](https://www.frankfurter.app/). It also keeps a history of all conversions in a file, so the user can see them even after closing the program.

This project was made for the VITyarthi *Build Your Own Project* evaluation.

## Features
- Live currency conversion between 30 currencies
- Currency list with full names and symbols
- Search currency by name or code
- Conversion history saved in `history.json` (latest 50 conversions)
- Clear history option
- Input validation (wrong code, negative amount, text instead of number)
- Error handling for no internet / API problems
- Logging of events and errors in `app.log`
- Unit tests

## Technologies Used
- Python 3.8 or above
- `requests` library (calls the API)
- `json`, `logging`, `datetime`, `math`, `os` (built-in modules)
- `unittest` (testing)
- Git and GitHub (version control)

## Project Structure
```
currency_converter/
├── main.py              # menu and program loop
├── converter.py         # conversion feature
├── currencies.py        # currency data, list and search
├── api_handler.py       # gets the rate from the API
├── validator.py         # input checking
├── history_manager.py   # saves / loads history
├── logger_setup.py      # logging setup
├── config.py            # settings
├── requirements.txt
├── statement.md
├── tests/
│   ├── test_validator.py
│   ├── test_converter.py
│   └── test_history.py
├── docs/                # diagrams
└── screenshots/
```

## How to Install and Run
1. Install Python 3 from https://www.python.org
2. Download or clone this repository:
   ```
   git clone <your-repository-link>
   cd currency_converter
   ```
3. Install the required library:
   ```
   pip install -r requirements.txt
   ```
4. Run the program (internet is needed for conversion):
   ```
   python main.py
   ```

## How to Use
1. Choose `1` for conversion, then enter the FROM code (e.g. `USD`), TO code (e.g. `INR`) and the amount.
2. Choose `2` to see all supported currency codes.
3. Choose `3` to search, for example `yen` or `eur`.
4. Choose `4` to see the history, `5` to clear it, `6` to exit.

## How to Run the Tests
From the main project folder run:
```
python -m unittest discover -s tests -t . -v
```
The tests check the validator, the calculation, the search and the history file. They do not need internet.

Manual test cases (need internet) are listed in the project report.

## Screenshots
Currency Converting:

<img width="634" height="258" alt="Screenshot 2026-09-30 212624" src="https://github.com/user-attachments/assets/923e4c33-dedb-4a53-905d-b347e3bafc4b" />

Currency not found:

<img width="600" height="174" alt="Screenshot 2026-09-30 212656" src="https://github.com/user-attachments/assets/af86bbbb-2ce1-443e-b861-100526231c1d" />

currency code to name or vice-versa:

<img width="654" height="168" alt="Screenshot 2026-09-30 212720" src="https://github.com/user-attachments/assets/fd0bb015-cbf7-4e3c-9320-44103fd22aab" />

Currency History:

<img width="640" height="224" alt="Screenshot 2026-09-30 212737" src="https://github.com/user-attachments/assets/dc03bde7-ec54-40b0-a9dd-cf6906ae06b1" />

Exit output:

<img width="667" height="188" alt="Screenshot 2026-09-30 212755" src="https://github.com/user-attachments/assets/e6d3a61b-7fe8-4d78-8e76-5056fc1bad5e" />

