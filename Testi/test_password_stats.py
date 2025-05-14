import unittest


from parolu_generators_un_parvaldnieks import PasswordStats

class TestPasswordStats(unittest.TestCase):
    
    def test_stats_calculation(self):
        """Test if password statistics are correctly calculated."""
        passwords = [
            {"password": "weak", "strength": "Vājš"},
            {"password": "Medium1", "strength": "Vidējs"},
            {"password": "Strong1!", "strength": "Spēcīgs"},
            {"password": "also_weak", "strength": "Vājš"}
        ]
        stats = PasswordStats(passwords)
        
        self.assertEqual(stats.weak, 2)
        self.assertEqual(stats.medium, 1)
        self.assertEqual(stats.strong, 1)
        self.assertEqual(stats.total, 4)
    
    def test_empty_passwords(self):
        """Test statistics with empty password list."""
        stats = PasswordStats([])
        
        self.assertEqual(stats.weak, 0)
        self.assertEqual(stats.medium, 0)
        self.assertEqual(stats.strong, 0)
        self.assertEqual(stats.total, 0)
    
    def test_missing_strength(self):
        """Test statistics with entries missing strength field."""
        passwords = [
            {"password": "weak"},  
            {"password": "Medium1", "strength": "Vidējs"},
            {"password": "another", "strength": None}  
        ]
        stats = PasswordStats(passwords)
        
        
        self.assertEqual(stats.weak, 0)
        self.assertEqual(stats.medium, 1)
        self.assertEqual(stats.strong, 0)
        self.assertEqual(stats.total, 3)  


if __name__ == "__main__":
    unittest.main()