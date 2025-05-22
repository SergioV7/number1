import unittest
import sys
import os

# Ensure the src directory is on the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import double


class TestDouble(unittest.TestCase):
    def test_double_positive(self):
        self.assertEqual(double(2), 4)

    def test_double_negative(self):
        self.assertEqual(double(-3), -6)


if __name__ == '__main__':
    unittest.main()
