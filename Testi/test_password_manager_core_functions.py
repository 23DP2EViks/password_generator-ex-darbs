import unittest
import os
import json
from unittest.mock import patch, MagicMock


from parolu_generators_un_parvaldnieks import PasswordManager

class TestPasswordManager(unittest.TestCase):
    
    def setUp(self):
        """Setup for each test - create a PasswordManager and remove test file."""
        self.manager = PasswordManager()
        self.test_file = "test_passwords.json"
        
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        
        if os.path.exists("passwords.json"):
            os.remove("passwords.json")
    
    def test_generate_and_check(self):
        """Test password generation and strength checking."""
        password = self.manager.generate(12, True, True, False, "")
        self.assertEqual(len(password), 12)
        strength = self.manager.check_strength(password)
        self.assertIn(strength, ["Vājš", "Vidējs", "Spēcīgs"])
        
        self.assertEqual(strength, "Spēcīgs")
    
    def test_save_and_load(self):
        """Test saving passwords to file and loading them back."""
        
        password1 = self.manager.generate(12, True, True, False, "")
        password2 = self.manager.generate(8, True, False, False, "")
        self.manager.save(self.test_file)
        
        
        self.assertTrue(os.path.exists(self.test_file))
        
        with open(self.test_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        self.assertEqual(len(data), 2)
        saved_passwords = [entry["password"] for entry in data]
        self.assertIn(password1, saved_passwords)
        self.assertIn(password2, saved_passwords)
    
    def test_clear_file(self):
        """Test clearing password file."""
        
        self.manager.generate(12, True, True, False, "")
        self.manager.save(self.test_file)
               
        self.manager.clear_file(self.test_file)
        
        with open(self.test_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        self.assertEqual(len(data), 0)


if __name__ == "__main__":
    unittest.main()