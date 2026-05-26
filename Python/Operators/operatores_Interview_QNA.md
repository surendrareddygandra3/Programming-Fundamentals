## 📘 Basic-Level Interview Questions on Python Operators
 
---
 
### 1. What are operators in Python?
#### ✅ Explanation:
Operators are special symbols used to perform operations on variables and values. Python supports various types of operators to perform arithmetic, logical, comparison, and assignment operations.
 
#### 💡 Real-Time Scenario:
Think of operators like tools in a calculator—`+` for addition, `*` for multiplication, etc.
 
#### 🔢 Code Example:
```python
a = 10
b = 5
print(a + b)  # Output: 15
```

### 2. List and explain the types of operators available in Python.
 
| Type                 | Description                    | Example         |
|----------------------|--------------------------------|-----------------|
| Arithmetic Operators | Perform mathematical operations| `+`, `-`, `*`    |
| Comparison Operators | Compare two values             | `==`, `!=`, `>`  |
| Logical Operators    | Combine conditional statements | `and`, `or`, `not` |
| Assignment Operators | Assign values to variables     | `=`, `+=`, etc. |
| Identity Operators   | Compare object identities      | `is`, `is not`  |
| Membership Operators | Test membership in a sequence  | `in`, `not in`  |
| Bitwise Operators    | Perform bit-level operations   | `&`, `|`, `^`    |
 
---
 
### 3. What is the difference between `=` and `==` operators?
#### ✅ Explanation:
- `=` is an **assignment operator** that assigns a value to a variable.
- `==` is a **comparison operator** that checks if two values are equal.
 
#### 💡 Real-Time Scenario:
Assigning your age: `age = 25`  
Checking if your age is 25: `age == 25`
 
#### 🔢 Code Example:
```python
x = 5       # Assignment
print(x == 5)  # Comparison → True
```
---

## 4. Arithmetic Operators
 
Arithmetic operators are used to perform mathematical operations.
 
| Operator | Description         | Example (`a = 10, b = 3`) | Result |
|----------|---------------------|---------------------------|--------|
| `+`      | Addition             | `a + b`                   | 13     |
| `-`      | Subtraction          | `a - b`                   | 7      |
| `*`      | Multiplication       | `a * b`                   | 30     |
| `/`      | Division             | `a / b`                   | 3.33   |
| `//`     | Floor Division       | `a // b`                  | 3      |
| `%`      | Modulus              | `a % b`                   | 1      |
| `**`     | Exponentiation       | `a ** b`                  | 1000   |
 
### 🔢 Code Example
```python
a = 10
b = 3
print(a + b, a % b, a ** b)
```
---

## 5. What are Comparison (Relational) Operators?
 
Comparison operators are used to compare two values and return either `True` or `False`.
 
| Operator | Meaning                     | Example (a = 5, b = 7) | Result  |
|----------|-----------------------------|------------------------|---------|
| `==`     | Equal to                    | `a == b`               | False   |
| `!=`     | Not equal to                | `a != b`               | True    |
| `>`      | Greater than                | `a > b`                | False   |
| `<`      | Less than                   | `a < b`                | True    |
| `>=`     | Greater than or equal to    | `a >= b`               | False   |
| `<=`     | Less than or equal to       | `a <= b`               | True    |
 
---
 
## 6. What is the use of Logical Operators in Python?
 
Logical operators are used to combine multiple conditional statements.
 
| Operator | Description                   | Example (a = 5, b = 10)       | Result |
|----------|-------------------------------|--------------------------------|--------|
| `and`    | Returns `True` if both are `True` | `a < 10 and b > 5`         | True   |
| `or`     | Returns `True` if at least one is `True` | `a > 10 or b > 5`   | True   |
| `not`    | Reverses the result              | `not(a > 10)`               | True   |
 
### 💡 Real-Time Scenario
You can use logical operators to check login credentials:
> Example: Login is successful only if both username and password are correct.
 
### 🔢 Code Example
```python
a = 5
b = 10
print(a < 10 and b > 5)  # Output: True

```
---

7. ### Explain Identity Operators: is and is not
Identity operators are used to compare the memory location of two objects.
 
| Operator  | Description   |	Example |	Result |
|-----------|--------------- ------------------|--------|---------|
| is	| True if both refer to the same object	| x is y |	True |
| is not | 	True if both refer to different objects |	x is not z	| True |
 
💡 Real-Time Scenario
Two people may have the same name (==), but they are not the same person (is not).
 
🔢 Code Example
```python
x = [1, 2]
y = x
z = [1, 2]
 
print(x is y)   # Output: True
print(x is z)   # Output: False
```
---

### 8. What is the difference between is and ==?
|Operator	| Compares	    |Example	| Result |
|--------------|--------------|----------|---------|
|== |	Compares values	| [1, 2] == [1, 2] |	True |
| is |	Compares memory locations |	[1, 2] is [1, 2] |	False |

---
### 9. What are Membership Operators? How do they work?
Membership operators test if a value exists in a sequence like a list, tuple, or string.
 
Operator 	Meaning	Example (x = [1, 2, 3])	Result
in	Exists in the object	2 in x	True
not in	Doesn't exist	5 not in x	True
 
🔢 Code Example
```python
x = [1, 2, 3]
print(2 in x)       # Output: True
print(5 not in x)   # Output: True
```
---

### 10. What are Assignment Operators? List a few with examples.
Assignment operators are used to assign values and perform operations in-place.
 
| Operator |   Description	     |Example (x = 10) | Result |
|----------|---------------------|-----------------|--------|
|    =	   |  Assign value	     | x = 5	       |   5    |
|   +=	   | Add and assign	     | x += 2	       |   12   |
|   -=     | Subtract and assign | x -= 3	       |   7    |
|   *=	   |Multiply and assign	 | x *= 2	       |  20    |
|   /=	   | Divide and assign	 | x /= 5	       |  2.0   |
|   **=    | 	Power and assign |	x **= 2	       | 100    |
 
🔢 Code Example
```python
x = 10
x += 5
print(x)  # Output: 15
```

---
## 11. How do bitwise operators work in Python?
### Theory:
Bitwise operators perform operations on the binary representation of integers.
 
Operator Name Example Result (for a = 5, b = 3)
& AND a & b 1
` ` OR `a
^ XOR a ^ b 6
~ NOT ~a -6
<< Left Shift a << 1 10
>> Right Shift a >> 1 2
 
### Real-time Scenario:
To manage permission flags in systems (like read/write/execute).
 
### Code:
 
```python

a = 5  # 0101
b = 3  # 0011
 
print("AND:", a & b)  # 0001 -> 1
print("OR:", a | b)   # 0111 -> 7
print("XOR:", a ^ b)  # 0110 -> 6
print("NOT:", ~a)     # -6 (2's complement)
print("Left Shift:", a << 1)  # 1010 -> 10
print("Right Shift:", a >> 1) # 0010 -> 2
```
---
## 12. Explain the use of and, or, not with truth tables.
### Theory:
 
A B A and B A or B not A
True True True True False
True False False True False
False True False True True
False False False False True
 
Real-time Scenario:
Login check: both username and password should be valid → and.
 
### Code:
 
```python

username = "admin"
password = "1234"
 
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")
```
---
## 13. How do operator precedence and associativity affect expression evaluation?
### Theory:
Operator precedence defines which operation is performed first.
Associativity resolves tie when operators have the same precedence (left to right or right to left).
 
Real-time Scenario:
Math expressions: 2 + 3 * 4 → Multiplication first.
 
### Code:
 
```python

result = 2 + 3 * 4
print(result)  # 14 (not 20)
 
# Using parentheses
result = (2 + 3) * 4
print(result)  # 20
```
## 14. How can parentheses alter the order of operations?
### Theory:
Parentheses override normal operator precedence.
 
Real-time Scenario:
Billing calculation: Add discount first, then apply tax.
 
### Code:
 
```python

price = 100
discount = 10
tax = 0.18
 
# Without parentheses
final_price = price - discount * (1 + tax)
print(final_price)  # 81.8
 
# With correct parentheses
final_price = (price - discount) * (1 + tax)
print(final_price)  # 106.2
```
## 15. Can Python operators be overloaded? Give examples.
### Theory:
Yes, operators can be overloaded using special methods like __add__, __mul__, etc.
 
Real-time Scenario:
Adding two custom Vector objects.
 
### Code:
 
```python

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
 
    def __str__(self):
        return f"({self.x}, {self.y})"
 
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Output: (4, 6)
```
---
## 16. What is short-circuit evaluation in logical operators?
### Theory:
In and and or, Python stops evaluating as soon as the result is determined.
 
### Real-time Scenario:
Avoiding error due to None or missing values.
 
### Code:
 
```python

x = None
 
#Short-circuit prevents error
if x is not None and x > 5:
    print("Greater than 5")
 
#Without short-circuit, this would cause an error
```
---
## 17. What happens if you compare different data types using relational operators?
### Theory:
Python allows comparison between compatible types but throws an error for incompatible ones (like string vs int in Python 3).
 
### Real-time Scenario:
Validating user input types.
 
### Code:
 
```python

print(5 > 3.2)      # True (int vs float)
print("a" < "b")    # True (string comparison)
# print("5" > 3)    # TypeError: unorderable types
```
---
## 18. How are chained comparisons handled in Python (e.g., 3 < x < 10)?
### Theory:
Chained comparisons are evaluated logically: 3 < x < 10 means 3 < x and x < 10.
 
### Real-time Scenario:
Checking if marks are in a valid range.
 
### Code:
 
```python

x = 7
if 3 < x < 10:
    print("x is in range")
else:
    print("x is out of range")
```
---
## 19. How does Python handle the in operator with dictionaries?
### Theory:
in checks whether a key exists in the dictionary, not the value.
 
### Real-time Scenario:
Checking if a user is already registered.
 
### Code:
 
```python

users = {"user1": "admin", "user2": "guest"}
 
print("user1" in users)      # True
print("admin" in users)      # False
```
---
## 20. Can assignment operators be used in expressions?
### Theory:
Yes. Assignment expressions using := (walrus operator) can be used in Python 3.8+.
 
### Real-time Scenario:
Reading input while assigning in the same expression.
 
### Code:
 
```python

# Example using walrus operator
while (line := input("Enter: ")) != "exit":
    print(f"You entered: {line}")
```
-------
## 21. How do custom classes implement operator overloading?
### Theory:
Custom classes overload operators by defining special methods like __add__, __eq__, etc.
 
### Real-time Scenario:
You want to add two Point objects with +.
 
### Code:
 
```python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
 
p1 = Point(2, 3)
p2 = Point(1, 4)
print(p1 + p2)  # Output: (3, 7)
```
---
## 22. What are magic methods (dunder methods) used for operator overloading?
### Theory:
Magic methods (double underscores or “dunders”) implement Python's built-in behavior.
### Examples:
 
__add__() for +
 
__eq__() for ==
 
__lt__() for <
 
__str__() for str()
 
### Code:
 
```python
class Box:
    def __init__(self, volume):
        self.volume = volume
    
    def __lt__(self, other):
        return self.volume < other.volume
 
b1 = Box(100)
b2 = Box(150)
print(b1 < b2)  # True
```
---
## 23. How do you implement custom comparison logic in a class?
### Theory:
Use comparison dunder methods like __lt__, __gt__, __eq__, etc.
 
### Real-time Scenario:
Sorting employee objects by salary.
 
### Code:
 
```python
class Employee:
    def __init__(self, name, salary):
self.name = name
        self.salary = salary
    
    def __lt__(self, other):
        return self.salary < other.salary
 
emp1 = Employee("A", 30000)
emp2 = Employee("B", 40000)
print(emp1 < emp2)  # True
```
---
## 24. How does the is operator behave with immutable vs mutable types?
### Theory:
 
is checks identity (memory location), not equality.
 
For immutables (like small integers or strings), Python reuses objects.
 
### Code:
 
```python
a = 100
b = 100
print(a is b)  # True (small integer caching)
 
x = [1, 2]
y = [1, 2]
print(x is y)  # False (different memory addresses)
print(x == y)  # True (same content)
```
---
## 25. What are some common pitfalls with using logical operators in conditions?
### Theory:
 
Using and instead of or, or vice versa.
 
Misusing truthy/falsy values.
 
Not considering short-circuit behavior.
 
### Code:
 
```python
# Pitfall: unintended short-circuit
a = None
if a and a > 5:
    print("Won't run")  # Avoided error due to short-circuit
```
---
## 26. Can you give real-world use cases for each type of operator in a project?
|Operator Type| Use Case|
|-------------|---------|
|Arithmetic | Calculating totals, discounts in billing apps|
|Comparison |Validating inputs, thresholds|
|Logical |Authentication conditions|
|Bitwise |Permissions & flags in system programming|
|Assignment |Updating variables in loops|
|Membership |Checking item in list/cart|
|Identity |Caching or object tracking|
|Ternary |Inline status checks (e.g., success/failure)|
---
## 27. How can misuse of is vs == cause bugs in Python programs?
### Theory:
 
is checks identity, not content.
 
Use == to compare values.
 
### Code:
 
```python
a = "hello"
b = "".join(["he", "llo"])
 
print(a == b)  # True
print(a is b)  # False (not same object)
 
# Bug: using `is` may fail value comparison
```
---
## 28. What are ternary (conditional) operators in Python?
### Theory:
A one-line if-else expression.
Syntax: x if condition else y
 
### Real-time Scenario:
Show status based on marks.
 
## Code:
 
```python
marks = 85
status = "Pass" if marks >= 40 else "Fail"
print(status)  # Pass
```
---
## 29. What is the walrus operator (:=) introduced in Python 3.8?
### Theory:
Assigns a value within an expression.
 
### Real-time Scenario:
Read and assign input in a loop.
 
### Code:
 
```python
# Classic
while True:
    line = input()
    if line == "exit":
        break
 
# Using walrus operator
while (line := input()) != "exit":
    print(f"You typed: {line}")
```
---
## 30. How do operators behave differently in Python 2 vs Python 3?
|Operator |Python 2 |Python 3|
|---------|---------|---------|
|/ Division| Integer if both operands are int Always |float division
|// Floor Division| Same| Same
|print Statement| (print "hello") |Function (print("hello"))
|unicode vs str| Two types Unified| str in Python 3
 
### Code Difference:
```python
# Python 2
print 5 / 2  # 2
 
# Python 3
print(5 / 2)  # 2.5
```
---