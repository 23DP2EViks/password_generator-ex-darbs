import unittest

from parolu_generators_un_parvaldnieks import check_password_strength

class TestPasswordStrength(unittest.TestCase):
    
    def test_strong_password(self):
        """Test if strong password is correctly identified."""
        password = "Abc123!@#XYZ"  
        self.assertEqual(check_password_strength(password), "Spēcīgs")
    
    def test_medium_password(self):
        """Test if medium password is correctly identified."""
        password1 = "Abcdefghijkl"  
        password2 = "abcde12345!@"  
        self.assertEqual(check_password_strength(password1), "Vidējs")
        self.assertEqual(check_password_strength(password2), "Vidējs")
    
    def test_weak_password(self):
        """Test if weak password is correctly identified."""
        password = "password123"  
        self.assertEqual(check_password_strength(password), "Vājš")
    
    def test_edge_cases(self):
        """Test edge cases for password strength."""
        
        short_strong = "A1!"
        self.assertEqual(check_password_strength(short_strong), "Vājš")
        
        long_missing_upper = "abcdefghijkl123!@#"
        self.assertEqual(check_password_strength(long_missing_upper), "Vidējs")


if __name__ == "__main__":
    unittest.main()