# api_handler.py
# Talks to the Frankfurter API to get the exchange rate

import requests
from config import API_URL, REQUEST_TIMEOUT
from logger_setup import setup_logger

logger = setup_logger()


def get_rate(from_currency, to_currency):
    """
    Returns the exchange rate as a float.
    Returns None if something goes wrong (error is written in the log).
    """
    url = f"{API_URL}?from={from_currency}&to={to_currency}"

    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)

        if response.status_code != 200:
            logger.error(f"API returned status {response.status_code} for {url}")
            return None

        data = response.json()

        if "rates" not in data or to_currency not in data["rates"]:
            logger.error(f"Rate missing in API response: {data}")
            return None

        logger.info(f"Rate fetched: 1 {from_currency} = {data['rates'][to_currency]} {to_currency}")
        return data["rates"][to_currency]

    except requests.exceptions.Timeout:
        logger.error("Request timed out")
        return None

    except requests.exceptions.RequestException as e:
        logger.error(f"Network problem: {e}")
        return None
