# cross-multiply-3digit

三位數交叉相乘＋逐位進位演算法的輕量級 Python 開源實作（零外部依賴）。

## 演算法原理

設兩個三位數為 A = a₁a₂a₃ 與 B = b₁b₂b₃，透過五步交叉相乘並由低位向高位逐位進位求得結果：

1. **個位**：a₃ × b₃
2. **十位**：a₂ × b₃ + a₃ × b₂
3. **百位**：a₁ × b₃ + a₂ × b₂ + a₃ × b₁
4. **千位**：a₁ × b₂ + a₂ × b₁（含兩位數進位處理，如 `999 × 999` 進位 `16`）
5. **萬位**：a₁ × b₁

## 快速使用

```python
from cross_multiply_3digit import cross_multiply_3digit

result = cross_multiply_3digit(123, 456)
print(result)  # 輸出: 56088
```

## 執行測試

本專案包含 4 項單元測試（已知案例、第四步進位 16、隨機 1,000 次測試、無效輸入檢查）：

```bash
python -m unittest discover -s tests
```

## 授權條款

本專案採用 [MIT License](LICENSE) 釋出。
