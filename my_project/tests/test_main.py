import unittest
from my_project.src.main import double

class TestDouble(unittest.TestCase):
    def test_double_positive(self):
        self.assertEqual(double(2), 4)
        self.assertEqual(double(0), 0)
        self.assertEqual(double(-3), -6)

if __name__ == "__main__":
    unittest.main()
