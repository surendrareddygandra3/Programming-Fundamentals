# Python Operators Explained
 
Operators in Python are special symbols or keywords used to perform operations on variables and values. Python supports the following categories of operators:
 
---
 
## 1. **Arithmetic Operators**
 
Used to perform basic mathematical operations.
 
| Operator | Description         | Example         | Result |
|----------|---------------------|------------------|--------|
| `+`      | Addition             | `10 + 5`         | `15`   |
| `-`      | Subtraction          | `10 - 5`         | `5`    |
| `*`      | Multiplication       | `10 * 5`         | `50`   |
| `/`      | Division             | `10 / 5`         | `2.0`  |
| `//`     | Floor Division       | `10 // 3`        | `3`    |
| `%`      | Modulus              | `10 % 3`         | `1`    |
| `**`     | Exponentiation       | `2 ** 3`         | `8`    |
 
### 📌 Scenario:
Calculating bill totals, tax, and discounts in a shopping cart.
 
---
 
## 2. **Comparison (Relational) Operators**
 
Used to compare two values.
 
| Operator | Description             | Example     | Result |
|----------|-------------------------|-------------|--------|
| `==`     | Equal to                | `5 == 5`     | `True` |
| `!=`     | Not equal to            | `5 != 3`     | `True` |
| `>`      | Greater than            | `5 > 3`      | `True` |
| `<`      | Less than               | `5 < 3`      | `False`|
| `>=`     | Greater than or equal to| `5 >= 5`     | `True` |
| `<=`     | Less than or equal to   | `5 <= 6`     | `True` |
 
### 📌 Scenario:
Used in conditions like eligibility checks, scores comparison.
 
---
 
## 3. **Assignment Operators**
 
Used to assign values to variables.
 
| Operator | Description             | Example       | Equivalent |
|----------|-------------------------|---------------|------------|
| `=`      | Assign                  | `x = 5`       | -          |
| `+=`     | Add and assign          | `x += 3`      | `x = x + 3`|
| `-=`     | Subtract and assign     | `x -= 2`      | `x = x - 2`|
| `*=`     | Multiply and assign     | `x *= 4`      | `x = x * 4`|
| `/=`     | Divide and assign       | `x /= 2`      | `x = x / 2`|
| `//=`    | Floor divide and assign | `x //= 2`     | `x = x // 2`|
| `%=`     | Modulus and assign      | `x %= 3`      | `x = x % 3`|
| `**=`    | Power and assign        | `x **= 2`     | `x = x ** 2`|
 
---
 
## 4. **Logical Operators**
 
Used to combine conditional statements.
 
| Operator | Description      | Example              | Result |
|----------|------------------|-----------------------|--------|
| `and`    | Logical AND      | `True and False`      | `False`|
| `or`     | Logical OR       | `True or False`       | `True` |
| `not`    | Logical NOT      | `not True`            | `False`|
 
### 📌 Scenario:
Used in filtering data (e.g., users who are both active **and** subscribed).
 
---
 
## 5. **Bitwise Operators**
 
Operate on bits and perform bit-by-bit operations.
 
| Operator | Description         | Example      | Binary Result |
|----------|---------------------|--------------|----------------|
| `&`      | AND                 | `5 & 3`      | `1` (`0101 & 0011`) |
| `|`      | OR                  | `5 | 3`      | `7` (`0101 | 0011`) |
| `^`      | XOR                 | `5 ^ 3`      | `6`             |
| `~`      | NOT                 | `~5`         | `-6` (inverts bits)|
| `<<`     | Left shift          | `5 << 1`     | `10`            |
| `>>`     | Right shift         | `5 >> 1`     | `2`             |
 
---
 
## 6. **Membership Operators**
 
Test whether a value exists in a sequence.
 
| Operator | Description             | Example           | Result |
|----------|-------------------------|--------------------|--------|
| `in`     | Present in sequence     | `'a' in 'apple'`   | `True` |
| `not in` | Not present in sequence | `'x' not in 'box'` | `False`|
 
---
 
## 7. **Identity Operators**
 
Compare the memory locations of two objects.
 
| Operator | Description      | Example           | Result |
|----------|------------------|--------------------|--------|
| `is`     | Same object      | `x is y`           | `True/False` |
| `is not` | Not same object  | `x is not y`       | `True/False` |
 
---
 
## 8. **Ternary (Conditional) Operator**
 
Used for inline conditional expressions.
 
```python
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)  # Output: Even
```
-----