def cross_multiply_3digit(a: int, b: int) -> int:
    """
    三位數交叉相乘＋逐位進位演算法 (3-Digit Cross-Multiplication)
    
    計算步驟（設 a = a1 a2 a3, b = b1 b2 b3）：
    1. 個位：a3 * b3
    2. 十位：a2 * b3 + a3 * b2
    3. 百位：a1 * b3 + a2 * b2 + a3 * b1
    4. 千位：a1 * b2 + a2 * b1（包含大於等於 10 的逐位進位，如進位 16）
    5. 萬位：a1 * b1
    """
    if isinstance(a, bool) or isinstance(b, bool) or not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("輸入必須為整數")
    if not (100 <= a <= 999 and 100 <= b <= 999):
        raise ValueError("輸入必須為 100 到 999 之間的三位正整數")

    a1, a2, a3 = a // 100, (a // 10) % 10, a % 10
    b1, b2, b3 = b // 100, (b // 10) % 10, b % 10

    s1 = a3 * b3
    s2 = a2 * b3 + a3 * b2
    s3 = a1 * b3 + a2 * b2 + a3 * b1
    s4 = a1 * b2 + a2 * b1
    s5 = a1 * b1

    d1 = s1 % 10
    c1 = s1 // 10

    t2 = s2 + c1
    d2 = t2 % 10
    c2 = t2 // 10

    t3 = s3 + c2
    d3 = t3 % 10
    c3 = t3 // 10

    t4 = s4 + c3
    d4 = t4 % 10
    c4 = t4 // 10

    t5 = s5 + c4

    return t5 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1


if __name__ == "__main__":
    print(f"123 x 456 = {cross_multiply_3digit(123, 456)}")
    print(f"999 x 999 = {cross_multiply_3digit(999, 999)}")
  
