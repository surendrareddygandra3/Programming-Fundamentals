# Python Interview Questions: Operators (Client-Focused)
 
This section provides **Python Operators** interview questions followed by code examples, structured from **basic to advanced** levels.
 
---
 
## 📘 Basic-Level Interview Questions and Code Examples
 
1. **What are operators in Python? Give some basic examples.**
 
```python
# Arithmetic Operators
x = 10
y = 3
print(x + y)  # 13
print(x - y)  # 7
print(x * y)  # 30
print(x / y)  # 3.333...
```
 
2. **What is the difference between `==` and `=` operators?**
 
```python
# '=' is assignment, '==' is comparison
x = 5       # assignment
print(x == 5)  # True (comparison)
```
 
3. **What is the purpose of the `//` and `%` operators?**
 
```python
print(10 // 3)  # 3 (floor division)
print(10 % 3)   # 1 (modulus)
```
 
4. **Explain the `**` operator in Python.**
 
```python
print(2 ** 3)  # 8 (exponentiation)
```
 
5. **What are relational (comparison) operators in Python?**
 
```python
x = 10
y = 20
print(x < y)   # True
print(x >= y)  # False
```
 
6. **What are logical operators in Python?**
 
```python
x = 5
y = 10
print(x < y and x > 0)  # True
print(x > y or x == 5)  # True
print(not(x < y))       # False
```
 
7. **What are bitwise operators?**
 
```python
a = 5   # 0101
b = 3   # 0011
print(a & b)  # 1 (0001)
print(a | b)  # 7 (0111)
print(a ^ b)  # 6 (0110)
```
 
8. **How does the `not` operator work?**
 
```python
x = True
print(not x)  # False
```
 
9. **What is the difference between `is` and `==`?**
 
```python
x = [1, 2]
y = [1, 2]
print(x == y)  # True (same value)
print(x is y)  # False (different objects)
```
 
10. **What are identity operators?**
 
```python
a = [1, 2]
b = a
print(a is b)      # True
print(a is not b)  # False
```
 
---
 
## 🧩 Intermediate-Level Interview Questions and Code Examples
 
11. **Explain membership operators with examples.**
 
```python
fruits = ['apple', 'banana']
print('apple' in fruits)   # True
print('mango' not in fruits)  # True
```
 
12. **Can we combine different types of operators? Give an example.**
 
```python
x = 10
y = 5
print((x > y) and (x != 0))  # True
```
 
13. **How are operator precedence and associativity handled in Python?**
 
```python
result = 3 + 2 * 2  # 7 (multiplication has higher precedence)
print(result)
```
 
14. **What are compound assignment operators?**
 
```python
x = 5
x += 3  # x = x + 3 => 8
print(x)
```
 
15. **How do you use the ternary operator (conditional expression)?**
 
```python
x = 10
y = 20
result = x if x > y else y
print(result)  # 20
```
 
16. **How are chained comparisons handled in Python?**
 
```python
x = 5
print(1 < x < 10)  # True
```
 
17. **What happens if we divide by zero?**
 
```python
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(e)  # division by zero
```
 
18. **How do boolean operators behave with non-boolean values?**
 
```python
print(0 and 5)      # 0
print(5 and 0)      # 0
print(5 or 0)       # 5
print(0 or 5)       # 5
```
 
19. **How does Python handle operator overloading?**
 
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
 
p1 = Point(1, 2)
p2 = Point(3, 4)
result = p1 + p2
print(result.x, result.y)  # 4 6
```
 
20. **What are some pitfalls in using `is` vs `==` with strings or numbers?**
 
```python
x = "hello"
y = "hello"
print(x == y)  # True
print(x is y)  # True in CPython due to string interning
 
x = 256
y = 256
print(x is y)  # True
 
x = 257
y = 257
print(x is y)  # False (may vary)
```
 
---
 
## 🚀 Advanced-Level Interview Questions and Code Examples
 
21. **How does short-circuit evaluation work in logical operators?**
 
```python
def check():
    print("Function called")
    return True
 
x = False and check()  # check() is not called due to short-circuit
print(x)
```
 
22. **How do you use `operator` module for functional programming?**
 
```python
import operator
print(operator.add(2, 3))  # 5
print(operator.mul(2, 4))  # 8
```
 
23. **How do you create custom behavior using operator overloading?**
 
```python
class Book:
    def __init__(self, pages):
        self.pages = pages
 
    def __add__(self, other):
        return Book(self.pages + other.pages)
 
b1 = Book(100)
b2 = Book(150)
b3 = b1 + b2
print(b3.pages)  # 250
```
 
24. **How are operators affected by Python’s type system (e.g., str + int)?**
 
```python
# print("age" + 20)  # TypeError
print("age" + str(20))  # age20
```
 
25. **What is the result of bitwise NOT and why?**
 
```python
x = 5
print(~x)  # -6 (inverts all bits)
```
 
26. **What is the difference between `x += 1` and `x = x + 1`?**
 
```python
x = 5
x += 1
print(x)  # 6
 
x = 5
x = x + 1
print(x)  # 6
# Functionally same, `+=` is syntactic sugar
```
 
27. **What are walrus operators (`:=`) and where are they used?**
 
```python
# Introduced in Python 3.8
if (n := len("Hello")) > 3:
    print(f"Length is {n}")  # Length is 5
```
 
28. **How to simulate switch-case using operator module or mapping?**
 
```python
def add(x, y): return x + y
def sub(x, y): return x - y
 
dispatch = {
    'add': add,
    'sub': sub
}
 
print(dispatch['add'](5, 3))  # 8
```
 
29. **What are augmented assignments and how do they affect mutable types?**
 
```python
x = [1, 2, 3]
y = x
x += [4]
print(x)  # [1, 2, 3, 4]
print(y)  # [1, 2, 3, 4] (same object)
```
 
30. **What are real-world scenarios where operator misuse causes bugs?**
 
```python
x = "10"
y = 2
# print(x + y)  # TypeError
print(int(x) + y)  # 12
```
 
---
 