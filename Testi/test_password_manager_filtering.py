import unittest
import os
import json


from parolu_generators_un_parvaldnieks import PasswordManager

class TestPasswordManagerFiltering(unittest.TestCase):
    
    def setUp(self):
        """Setup for each test - create a PasswordManager and test file."""
        self.manager = PasswordManager()
        
        self.test_data = [
            {"password": "abc123", "strength": "Vājš"},
            {"password": "Abc123def", "strength": "Vidējs"},
            {"password": "Abc123!@#XYZ", "strength": "Spēcīgs"}
        ]
        
        with open("passwords.json", "w", encoding="utf-8") as file:
            json.dump(self.test_data, file, indent=4, ensure_ascii=False)
    
    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists("passwords.json"):
            os.remove("passwords.json")
    
    def test_filter_by_strength(self):
        """Test filtering passwords by strength."""
        
        weak = self.manager.filter_by_strength("Vājš")
        medium = self.manager.filter_by_strength("Vidējs")
        strong = self.manager.filter_by_strength("Spēcīgs")
        
        self.assertEqual(weak, ["abc123"])
        self.assertEqual(medium, ["Abc123def"])
        self.assertEqual(strong, ["Abc123!@#XYZ"])
    
    def test_search(self):
        """Test searching passwords by substring."""
        
        results = self.manager.search("abc")
        self.assertEqual(results, ["abc123"])
        
        results = self.manager.search("123")
        self.assertEqual(len(results), 3)  
        
       
        results = self.manager.search("XYZ")  
        self.assertEqual(results, ["Abc123!@#XYZ"])
        
        results = self.manager.search("nonexistent")  
        self.assertEqual(results, [])
    
    def test_file_not_found(self):
        """Test behavior when file is not found."""
        
        os.remove("passwords.json")
        
        results = self.manager.search("abc")
        self.assertEqual(results, [])
        
        filtered = self.manager.filter_by_strength("Spēcīgs")
        self.assertEqual(filtered, [])


if __name__ == "__main__":
    unittest.main()