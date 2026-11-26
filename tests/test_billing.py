import unittest
from src.billing import calculate_total

class TestBilling(unittest.TestCase):
    def test_standard_total(self):
        self.assertEqual(calculate_total(100.0), 110.0)

    def test_negative_subtotal_raises(self):
        with self.assertRaises(ValueError):
            calculate_total(-10.0)

if __name__ == "__main__":
    unittest.main()
