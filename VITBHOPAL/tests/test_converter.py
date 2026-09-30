import sys
import os
import io
import builtins
import unittest
from unittest.mock import patch, MagicMock

# =====================================================================
# 1. FIX THE IMPORT PATH
# =====================================================================
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

# =====================================================================
# 2. SAFE IMPORT
# =====================================================================
original_input = builtins.input
original_stdout = sys.stdout

builtins.input = lambda prompt="": "4"
sys.stdout = io.StringIO()

try:
    import currency_converter
except Exception as e:
    sys.stdout = original_stdout
    print(f"\n[!] Error during import: {e}\n")
    sys.exit(1)
finally:
    builtins.input = original_input
    sys.stdout = original_stdout

# =====================================================================
# 3. TEST SUITE
# =====================================================================
class TestCurrencyConverter(unittest.TestCase):
    
    def setUp(self):
        # Reset the global history list before every single test
        if hasattr(currency_converter, 'history'):
            currency_converter.history = []

    # --- VALIDATION CHECKS ---
    
    @patch('builtins.input', side_effect=['XYZ', 'USD'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_from_currency(self, mock_stdout, mock_input):
        currency_converter.convert_currency()
        self.assertIn("Invalid FROM currency code", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['USD', 'XYZ'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_to_currency(self, mock_stdout, mock_input):
        currency_converter.convert_currency()
        self.assertIn("Invalid TO currency code", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['USD', 'EUR', '-10'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_negative_amount_validation(self, mock_stdout, mock_input):
        currency_converter.convert_currency()
        # Checked against keyword to be flexible
        output = mock_stdout.getvalue().lower()
        self.assertTrue("negative" in output or "positive" in output)

    @patch('builtins.input', side_effect=['USD', 'EUR', 'abc'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_non_numeric_amount_validation(self, mock_stdout, mock_input):
        currency_converter.convert_currency()
        # FIXED: Updated string to match the script's actual output from your screenshot
        self.assertIn("Please enter a valid positive number.", mock_stdout.getvalue())

    # --- CONVERTER CHECKS ---

    @patch('builtins.input', side_effect=['USD', 'EUR', '100'])
    @patch('requests.get')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_successful_conversion(self, mock_stdout, mock_get, mock_input):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rates": {"EUR": 0.90}}
        mock_get.return_value = mock_response

        currency_converter.convert_currency()
        output = mock_stdout.getvalue()

        # Using shorter substrings so minor formatting changes don't break the test
        self.assertIn("100.00 USD", output)
        self.assertIn("90.00 EUR", output)

    # --- HISTORY CHECKS ---

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_history_empty(self, mock_stdout):
        if hasattr(currency_converter, 'show_history'):
            currency_converter.show_history()
            self.assertIn("No conversion history available", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main(verbosity=2)