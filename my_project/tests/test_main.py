import unittest
from my_project.src.main import double

class TestDouble(unittest.TestCase):
    def test_double_positive(self):
        self.assertEqual(double(2), 4)

    def test_double_negative(self):
        self.assertEqual(double(-3), -6)

    def test_double_zero(self):
        self.assertEqual(double(0), 0)

if __name__ == '__main__':
    unittest.main()
