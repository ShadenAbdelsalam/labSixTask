import unittest
from addCalc import add

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result1 = add(5, 5)
        result2 = add(-1, 0)
        self.assertEqual(result1, 10)
        self.assertEqual(result2, -1)

if __name__ == "__main__":
    unittest.main()
