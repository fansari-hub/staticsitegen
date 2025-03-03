import unittest
from generate_site import extract_title

class TestGenerateSite(unittest.TestCase):
    def test_extract_title_happypath(self):
        result = extract_title("# Tolkien Fan Club")
        excepted = "Tolkien Fan Club"
        self.assertEqual(result, excepted)

    def test_extract_title_nocontent(self):
        with self.assertRaises(Exception) as context:
            extract_title("")
        self.assertEqual(str(context.exception), "No content provided")

    def test_extract_title_badheader(self):
        with self.assertRaises(Exception) as context:
            extract_title("## Tolkien Fan Club")
        self.assertEqual(str(context.exception), "No level 1 header found at start!")

    def test_extract_title_badheader__multi_line(self):
        with self.assertRaises(Exception) as context:
            md = """### Tolkien Fan Club
Hello This is some Text.
And More text."""
            extract_title(md)
        self.assertEqual(str(context.exception), "No level 1 header found at start!")   

    def test_extract_title_happypath_multiline(self):
        md = """# Tolkien Fan Club
Hello This is some Text.
And More text."""        
        result = extract_title(md)
        excepted = "Tolkien Fan Club"
        self.assertEqual(result, excepted)     

if __name__ == "__main__":
    unittest.main()