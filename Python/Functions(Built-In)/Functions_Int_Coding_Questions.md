# Python Functions & Built-in Functions – Coding Questions with Answers
 
---
 
## ✅ Basic-Level Coding Questions (1–10)
 
---
 
### 1. Write a simple function to greet a user
```python
def greet(name):
    print("Hello", name)
 
greet("John")
```
**Output:**
```
Hello John
```
 
---
 
### 2. Function to return square of a number
```python
def square(n):
    return n * n
 
print(square(4))
```
**Output:**
```
16
```
 
---
 
### 3. Function with default arguments
```python
def greet(name="Guest"):
    print("Welcome", name)
 
greet()
greet("John")
```
**Output:**
```
Welcome Guest
Welcome John
```
 
---
 
### 4. Function to return multiple values
```python
def calc(a, b):
    return a + b, a - b
 
add, sub = calc(10, 5)
print(add, sub)
```
**Output:**
```
15 5
```
 
---
 
### 5. Function to find max of 3 numbers
```python
def find_max(a, b, c):
    return max(a, b, c)
 
print(find_max(10, 30, 20))
```
**Output:**
```
30
```
 
---
 
### 6. Check if a number is even using function
```python
def is_even(n):
    return n % 2 == 0
 
print(is_even(6))
```
**Output:**
```
True
```
 
---
 
### 7. Function to reverse a string
```python
def reverse_str(text):
    return text[::-1]
 
print(reverse_str("python"))
```
**Output:**
```
nohtyp
```
 
---
 
### 8. Function to check palindrome
```python
def is_palindrome(s):
    return s == s[::-1]
 
print(is_palindrome("madam"))
```
**Output:**
```
True
```
 
---
 
### 9. Use keyword arguments in function call
```python
def details(name, age):
    print(f"{name} is {age} years old")
 
details(age=25, name="John")
```
**Output:**
```
John is 25 years old
```
 
---
 
### 10. Sum of elements in a list using function
```python
def list_sum(lst):
    return sum(lst)
 
print(list_sum([1, 2, 3, 4]))
```
**Output:**
```
10
```
 
---
 
## ✅ Intermediate-Level Coding Questions (11–20)
 
---
 
### 11. Function with variable-length arguments (`*args`)
```python
def total(*args):
    return sum(args)
 
print(total(1, 2, 3, 4))
```
**Output:**
```
10
```
 
---
 
### 12. Function with `**kwargs`
```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
 
show_info(name="John", role="Developer")
```
**Output:**
```
name: John
role: Developer
```
 
---
 
### 13. Recursive function for factorial
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
 
print(factorial(5))
```
**Output:**
```
120
```
 
---
 
### 14. Lambda function to calculate cube
```python
cube = lambda x: x ** 3
print(cube(3))
```
**Output:**
```
27
```
 
---
 
### 15. Function to filter even numbers
```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
```
**Output:**
```
[2, 4, 6]
```
 
---
 
### 16. Use `map()` to square elements
```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares)
```
**Output:**
```
[1, 4, 9, 16]
```
 
---
 
### 17. Use `zip()` to merge two lists
```python
names = ["Alice", "Bob"]
scores = [85, 90]
zipped = list(zip(names, scores))
print(zipped)
```
**Output:**
```
[('Alice', 85), ('Bob', 90)]
```
 
---
 
### 18. Use `enumerate()` in a function
```python
def list_indexed(items):
    for i, val in enumerate(items):
        print(i, val)
 
list_indexed(['a', 'b', 'c'])
```
**Output:**
```
0 a
1 b
2 c
```
 
---
 
### 19. Closure function (inner function)
```python
def outer(x):
    def inner(y):
        return x + y
    return inner
 
add_10 = outer(10)
print(add_10(5))
```
**Output:**
```
15
```
 
---
 
### 20. Check if all items in list are positive
```python
lst = [1, 2, 3, 4]
print(all(x > 0 for x in lst))
```
**Output:**
```
True
```
 
---
 
## ✅ Advanced / Real-World Scenario-Based (21–30)
 
---
 
### 21. Decorator to log function call
```python
def log(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper
 
@log
def say_hello():
    print("Hello!")
 
say_hello()
```
**Output:**
```
Function is being called
Hello!
```
 
---
 
### 22. Use `any()` to check condition
```python
lst = [0, False, 1]
print(any(lst))
```
**Output:**
```
True
```
 
---
 
### 23. Validate password using function
```python
def validate(pwd):
    if len(pwd) < 6:
        return "Too short"
    if not any(char.isdigit() for char in pwd):
        return "No digit"
    return "Valid"
 
print(validate("abc12"))
print(validate("abc123"))
```
**Output:**
```
Too short
Valid
```
 
---
 
### 24. Get type of variable using `type()`
```python
x = 10
print(type(x))
```
**Output:**
```
<class 'int'>
```
 
---
 
### 25. Use `isinstance()` to validate input type
```python
def check(n):
    if isinstance(n, int):
        return "Valid int"
    return "Invalid type"
 
print(check(5))
```
**Output:**
```
Valid int
```
 
---
 
### 26. Function to apply discount
```python
def apply_discount(price, discount=10):
    return price - (price * discount / 100)
 
print(apply_discount(1000))
```
**Output:**
```
900.0
```
 
---
 
### 27. Calculate average using function
```python
def average(lst):
    return sum(lst) / len(lst)
 
print(average([10, 20, 30]))
```
**Output:**
```
20.0
```
 
---
 
### 28. Use `sorted()` with custom key
```python
words = ["apple", "banana", "fig"]
sorted_words = sorted(words, key=len)
print(sorted_words)
```
**Output:**
```
['fig', 'apple', 'banana']
```
 
---
 
### 29. Use `eval()` to calculate expression
```python
expr = "2 + 3 * 4"
result = eval(expr)
print(result)
```
**Output:**
```
14
```
 
---
 
### 30. Function to print Fibonacci series
```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
 
fib(5)
```
**Output:**
```
0 1 1 2 3
```
 
---