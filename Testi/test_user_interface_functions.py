import unittest
from unittest.mock import patch, MagicMock
from io import StringIO

from parolu_generators_un_parvaldnieks import ask_yes_no, display_password_table

class TestUserInterface(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['y'])
    def test_ask_yes_no_yes(self, mock_input):
        """Test ask_yes_no function with 'y' input."""
        result = ask_yes_no("Test question?")
        self.assertTrue(result)
        mock_input.assert_called_once_with("Test question?")
    
    @patch('builtins.input', side_effect=['n'])
    def test_ask_yes_no_no(self, mock_input):
        """Test ask_yes_no function with 'n' input."""
        result = ask_yes_no("Test question?")
        self.assertFalse(result)
        mock_input.assert_called_once_with("Test question?")
    
    @patch('builtins.input', side_effect=['invalid', 'y'])
    @patch('builtins.print')
    def test_ask_yes_no_invalid_then_valid(self, mock_print, mock_input):
        """Test ask_yes_no function with invalid input followed by valid input."""
        result = ask_yes_no("Test question?")
        self.assertTrue(result)
        self.assertEqual(mock_input.call_count, 2)
        
        mock_print.assert_called_with("\033[92mNepareiza ievade. Lūdzu ievadiet 'y' vai 'n'.\033[0m")
    
    @patch('builtins.print')
    def test_display_password_table_empty(self, mock_print):
        """Test display_password_table with empty list."""
        display_password_table([])
        mock_print.assert_called_with("\033[92mNav par ko rādīt.\033[0m")
    
    @patch('builtins.print')
    def test_display_password_table_with_data(self, mock_print):
        """Test display_password_table with data."""
        password_list = [
            {"password": "test123", "strength": "Vidējs"},
            {"password": "StrongP@ss!", "strength": "Spēcīgs"}
        ]
        display_password_table(password_list)
        
        self.assertGreater(mock_print.call_count, 5)  


if __name__ == "__main__":
    unittest.main()