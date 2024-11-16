import unittest
from addCalc import add

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result1 = add(3, 7)
        result2 = add(-1, 1)
        self.assertEqual(result1, 10)
        self.assertEqual(result2, 0)

if _name_ == "_main_":
    unittest.main()
