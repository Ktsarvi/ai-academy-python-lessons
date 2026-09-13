import unittest
from multiply import multiply


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(1.5, 2), 3.0)


if __name__ == "__main__":
    unittest.main()
