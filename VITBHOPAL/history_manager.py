# history_manager.py
# Saves and loads the conversion history in a JSON file

import json
import os
from datetime import datetime
from config import HISTORY_FILE, MAX_HISTORY
from logger_setup import setup_logger

logger = setup_logger()


def load_history():
    """Reads the history from the file. Returns an empty list if there is none."""
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as e:
        logger.error(f"Could not read history file: {e}")
        return []


def save_history(history):
    """Writes the history list to the file"""
    try:
        with open(HISTORY_FILE, "w") as file:
            json.dump(history, file, indent=4)
    except OSError as e:
        logger.error(f"Could not save history file: {e}")


def add_record(from_currency, to_currency, amount, result):
    """Adds one conversion to the history"""
    history = load_history()

    history.append({
        "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "result": result
    })

    # keep only the latest records
    if len(history) > MAX_HISTORY:
        history = history[-MAX_HISTORY:]

    save_history(history)


def show_history():
    history = load_history()

    print("\nCONVERSION HISTORY")

    if not history:
        print("No conversion history available.")
        return

    for item in history:
        print(
            f"{item['time']} | "
            f"{item['amount']} {item['from']} -> "
            f"{item['result']:.2f} {item['to']}"
        )


def clear_history():
    save_history([])
    logger.info("History cleared by user")
    print("History cleared.")
