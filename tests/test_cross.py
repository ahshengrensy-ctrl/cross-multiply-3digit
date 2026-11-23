import random
import unittest
from cross_multiply_3digit import cross_multiply_3digit


class TestCrossMultiply3Digit(unittest.TestCase):
    def test_known(self):
        """1. 已知乘法案例驗證"""
        self.assertEqual(cross_multiply_3digit(123, 456), 56088)
        self.assertEqual(cross_multiply_3digit(100, 100), 10000)
        self.assertEqual(cross_multiply_3digit(321, 654), 209934)

    def test_step4_carry(self):
        """2. 第四步進位 16 邊界案例驗證 (999 * 999)"""
        self.assertEqual(cross_multiply_3digit(999, 999), 998001)
        self.assertEqual(cross_multiply_3digit(987, 989), 976143)

    def test_random_1000(self):
        """3. 隨機測試 1,000 次驗證"""
        random.seed(42)
        for _ in range(1000):
            a = random.randint(100, 999)
            b = random.randint(100, 999)
            self.assertEqual(cross_multiply_3digit(a, b), a * b)

    def test_invalid(self):
        """4. 非三位數及無效輸入處理"""
        invalid_inputs = [
            (99, 123),
            (123, 1000),
            (-123, 456),
            (12.3, 456),
            ("123", 456),
            (True, 123),
        ]
        for a, b in invalid_inputs:
            with self.assertRaises(ValueError):
                cross_multiply_3digit(a, b)


if __name__ == "__main__":
    unittest.main()
  
