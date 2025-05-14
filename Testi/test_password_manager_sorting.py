import unittest
import os
import json

from parolu_generators_un_parvaldnieks import PasswordManager

class TestPasswordManagerSorting(unittest.TestCase):
    
    def setUp(self):
        """Setup for each test - create a PasswordManager and test file."""
        self.manager = PasswordManager()
        
        self.test_data = [
            {"password": "abcdefg", "strength": "Vājš"},
            {"password": "Abc123!@", "strength": "Spēcīgs"},
            {"password": "xyz", "strength": "Vājš"},
            {"password": "Medium1", "strength": "Vidējs"}
        ]
        
        with open("passwords.json", "w", encoding="utf-8") as file:
            json.dump(self.test_data, file, indent=4, ensure_ascii=False)
    
    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists("passwords.json"):
            os.remove("passwords.json")
    
    def test_sort_by_length(self):
        """Test sorting passwords by length."""
        sorted_pwds = self.manager.sort_passwords(by="length")
        
        
        passwords = [entry["password"] for entry in sorted_pwds]
        
        
        self.assertEqual(passwords[0], "xyz")
        
        
        longest_password = max((item["password"] for item in sorted_pwds), key=len)
        self.assertEqual(passwords[-1], longest_password)
        
        
        lengths = [len(pwd) for pwd in passwords]
        self.assertEqual(lengths, sorted(lengths))
    
    def test_sort_alphabetically(self):
        """Test sorting passwords alphabetically."""
        sorted_pwds = self.manager.sort_passwords(by="alphabet")
        
        
        passwords = [entry["password"] for entry in sorted_pwds]
        self.assertEqual(passwords, sorted(passwords))
    
    def test_sort_by_strength(self):
        """Test sorting passwords by strength."""
        sorted_pwds = self.manager.sort_passwords(by="strength")
        
        
        strengths = [entry["strength"] for entry in sorted_pwds]
        
        
        strength_order = {"Vājš": 0, "Vidējs": 1, "Spēcīgs": 2}
        strength_values = [strength_order[s] for s in strengths]
        
        self.assertEqual(strength_values, sorted(strength_values))
        
        
        self.assertEqual(sorted_pwds[0]["strength"], "Vājš")
        
        
        self.assertEqual(sorted_pwds[-1]["strength"], "Spēcīgs")
    
    def test_invalid_sort_type(self):
        """Test behavior with invalid sort type."""
        
        result = self.manager.sort_passwords(by="invalid_type")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()