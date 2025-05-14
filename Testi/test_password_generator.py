import unittest
import string


from parolu_generators_un_parvaldnieks import generate_password

class TestPasswordGeneration(unittest.TestCase):
    
    def test_password_length(self):
        """Test if generated password has the correct length."""
        for length in [8, 12, 16, 24]:
            password = generate_password(length=length)
            self.assertEqual(len(password), length)
    
    def test_minimum_requirements(self):
        """Test if generated password meets minimum requirements."""
        password = generate_password()
        
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(not c.isalnum() for c in password))
    
    def test_excluded_chars(self):
        """Test if excluded characters are not in the generated password."""
        excluded = "abc123"
        password = generate_password(excluded_chars=excluded)
        for char in excluded:
            self.assertNotIn(char, password)
    
    def test_rare_symbols(self):
        """Test if rare symbols are included when requested."""
        rare_symbols = "`:;~\\|[]{}'\""
        
        included = False
        for _ in range(50):
            password = generate_password(include_rare_symbols=True)
            if any(char in rare_symbols for char in password):
                included = True
                break
        self.assertTrue(included)
    
    def test_invalid_length(self):
        """Test if ValueError is raised for invalid length."""
        with self.assertRaises(ValueError):
            generate_password(length=3)  
        with self.assertRaises(ValueError):
            generate_password(length=129)  
    
    def test_no_digits(self):
        """Test password generation without digits."""
        password = generate_password(use_digits=False)
        self.assertFalse(any(c.isdigit() for c in password))
    
    def test_no_symbols(self):
        """Test password generation without symbols."""
        password = generate_password(use_symbols=False)
        self.assertTrue(all(c.isalnum() for c in password))
    
    def test_all_chars_excluded(self):
        """Test if ValueError is raised when all characters of a category are excluded."""
        with self.assertRaises(ValueError):
            generate_password(excluded_chars=string.ascii_lowercase)


if __name__ == "__main__":
    unittest.main()