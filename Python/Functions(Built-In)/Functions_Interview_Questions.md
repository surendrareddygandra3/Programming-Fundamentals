# Python Functions & Built-In Functions – Interview Questions (All Levels)
 
---
 
## ✅ Basic-Level Questions (1–10)
 
### 1. **What is a function in Python?**  
**Answer:**  
A function is a reusable block of code designed to perform a specific task, making code more organized and reducing repetition.
 
**Scenario:**  
You need to calculate tax in multiple places in your code — write it once as a function.
 
**Example:**
```python
def calculate_tax(amount):
    return amount * 0.18
```
 
---
 
### 2. **How do you define a function in Python?**  
**Answer:**  
Use the `def` keyword followed by the function name, parentheses, and a colon. The code block is indented.
 
**Scenario:**  
You want to define a function to greet users by name.
 
**Example:**
```python
def greet(name):
    print("Hello,", name)
```
 
---
 
### 3. **What is the purpose of the `return` statement in a function?**  
**Answer:**  
The `return` statement sends a value back to the caller and ends the function execution.
 
**Scenario:**  
Return the result of a calculation for further processing.
 
**Example:**
```python
def add(a, b):
    return a + b
 
result = add(10, 5)  # result = 15
```
 
---
 
### 4. **What is the difference between `return` and `print()` in a function?**  
**Answer:**  
- `return` gives output to the caller.
- `print()` displays it to the console, mainly for debugging or output.
 
**Scenario:**  
Use `return` to store output; use `print()` to show it.
 
**Example:**
```python
def square(x):
    return x * x
 
print(square(4))  # return value used in print()
```
 
---
 
### 5. **Can a function return multiple values in Python?**  
**Answer:**  
Yes, by separating return values with commas; they are returned as a tuple.
 
**Scenario:**  
Return both sum and product of two numbers.
 
**Example:**
```python
def operate(a, b):
    return a + b, a * b
 
s, p = operate(2, 3)  # s=5, p=6
```
 
---
 
### 6. **What is the difference between a function and a method?**  
**Answer:**  
- **Function**: Defined independently using `def`.  
- **Method**: Function that belongs to an object or class.
 
**Scenario:**  
Using `len()` (function) vs `str.upper()` (method).
 
**Example:**
```python
def greet():  # Function
    print("Hi")
 
"hello".upper()  # Method
```
 
---
 
### 7. **What is the use of `def` keyword?**  
**Answer:**  
`def` is used to define a new function.
 
**Scenario:**  
Create a reusable function for converting Celsius to Fahrenheit.
 
**Example:**
```python
def to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
```
 
---
 
### 8. **What happens if you don’t use a `return` statement in a function?**  
**Answer:**  
The function returns `None` by default.
 
**Scenario:**  
You mistakenly forget `return`, and the output is not what you expect.
 
**Example:**
```python
def add(a, b):
    result = a + b  # No return
 
print(add(2, 3))  # Output: None
```
 
---
 
### 9. **What are default arguments in Python functions?**  
**Answer:**  
Default arguments let you assign default values to parameters if no value is passed.
 
**Scenario:**  
A greeting function should use "Guest" if no name is provided.
 
**Example:**
```python
def greet(name="Guest"):
    print("Hello,", name)
 
greet()         # Hello, Guest
greet("Surya")  # Hello, Surya
```
 
---
 
### 10. **What are positional and keyword arguments?**  
**Answer:**  
- **Positional arguments** are matched by position.  
- **Keyword arguments** are matched by parameter name.
 
**Scenario:**  
Calling a function where order matters vs using parameter names for clarity.
 
**Example:**
```python
def profile(name, age):
    print(name, age)
 
profile("Ravi", 25)               # Positional
profile(age=30, name="Kiran")     # Keyword
```
 
---
 
## ✅ Intermediate-Level Questions (11–20)
 
### 11. **What are variable-length arguments (`*args`, `**kwargs`) in functions?**  
**Answer:**  
`*args` allows passing a variable number of **positional arguments**, and `**kwargs` allows a variable number of **keyword arguments** to a function.
 
**Scenario:**  
Pass any number of items to a bill calculator.
 
**Example:**
```python
def total_bill(*items):
    return sum(items)
 
print(total_bill(100, 200, 50))  # Output: 350
```
 
```python
def show_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
 
show_details(name="Ravi", age=30)
```
 
---
 
### 12. **What is recursion? Can you give a simple example?**  
**Answer:**  
Recursion is when a function calls itself to solve a smaller instance of a problem.
 
**Scenario:**  
Calculate factorial of a number.
 
**Example:**
```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
 
print(factorial(5))  # Output: 120
```
 
---
 
### 13. **How can you document a function using docstrings?**  
**Answer:**  
A docstring is a string literal placed right after the function definition to describe its purpose.
 
**Scenario:**  
Show function help using `help()` or IDE popups.
 
**Example:**
```python
def greet(name):
    """This function greets the user by name."""
    return f"Hello, {name}"
 
print(greet("John"))
```
 
---
 
### 14. **Can functions be assigned to variables in Python?**  
**Answer:**  
Yes. Functions are first-class objects in Python and can be assigned to variables.
 
**Scenario:**  
Create a shortcut for a commonly used function.
 
**Example:**
```python
def shout(text):
    return text.upper()
 
say = shout
print(say("hello"))  # Output: HELLO
```
 
---
 
### 15. **Can functions be passed as arguments to another function?**  
**Answer:**  
Yes. Functions can be passed like any other object.
 
**Scenario:**  
Apply different operations to a number.
 
**Example:**
```python
def apply(fn, value):
    return fn(value)
 
def double(x):
    return x * 2
 
print(apply(double, 5))  # Output: 10
```
 
---
 
### 16. **What are lambda functions? How are they different from `def` functions?**  
**Answer:**  
A lambda is an anonymous function defined using the `lambda` keyword, typically used for short, simple operations.
 
**Scenario:**  
Sort list of tuples by the second item.
 
**Example:**
```python
square = lambda x: x * x
print(square(4))  # Output: 16
 
pairs = [(1, 3), (2, 1), (3, 2)]
pairs.sort(key=lambda x: x[1])
print(pairs)  # [(2, 1), (3, 2), (1, 3)]
```
 
---
 
### 17. **What is the difference between local and global variables inside a function?**  
**Answer:**  
- **Local variables** are declared inside a function and only accessible within it.  
- **Global variables** are declared outside and accessible throughout the module.
 
**Scenario:**  
Modify a global counter inside a function.
 
**Example:**
```python
count = 10  # Global
 
def modify():
    global count
    count += 1
 
modify()
print(count)  # Output: 11
```
 
---
 
### 18. **How do closures and inner functions work in Python?**  
**Answer:**  
Closures allow inner functions to capture and remember values from their enclosing scope, even after the outer function has finished executing.
 
**Scenario:**  
Create a personalized greeting function.
 
**Example:**
```python
def outer(name):
    def inner():
        return f"Hello, {name}"
    return inner
 
greet = outer("Ravi")
print(greet())  # Output: Hello, Ravi
```
 
---
 
### 19. **What are pure functions?**  
**Answer:**  
A pure function always gives the same output for the same input and has **no side effects** (doesn’t modify global state or use I/O).
 
**Scenario:**  
Use in data pipelines or testing.
 
**Example:**
```python
def add(a, b):
    return a + b  # Pure function
 
print(add(2, 3))  # Output: 5
```
 
---
 
### 20. **Can a function call itself in Python? Why would you do that?**  
**Answer:**  
Yes. This is called **recursion** and is useful for solving problems that can be divided into smaller similar subproblems.
 
**Scenario:**  
Traverse tree or folder structures, compute Fibonacci.
 
**Example:**
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
 
print(fib(5))  # Output: 5
```
 
---
 
## ✅ Advanced / Real-Time / Scenario-Based Questions (21–30)
 
### 21. **What are decorators in Python and why are they useful?**  
**Answer:**  
A decorator is a function that takes another function and extends its behavior without changing the original code.
 
**Scenario:**  
Log whenever a function is called without modifying its code.
 
**Example:**
```python
def logger(func):
    def wrapper():
        print("Function called")
        return func()
    return wrapper
 
@logger
def greet():
    print("Hello")
 
greet()
```
 
---
 
### 22. **What is the difference between a built-in function and a user-defined function?**  
**Answer:**  
- **Built-in functions**: Provided by Python (`len()`, `sum()`)  
- **User-defined functions**: Created using `def` by the programmer
 
**Scenario:**  
Use `len()` to find the length of a list; write your own `calculate_tax()` function.
 
**Example:**
```python
print(len("Python"))  # Built-in
 
def calculate_tax(amount):  # User-defined
    return amount * 0.18
```
 
---
 
### 23. **Can you override built-in functions in Python? Should you?**  
**Answer:**  
Yes, but it’s **not recommended**. Overriding can lead to confusion and bugs.
 
**Scenario:**  
Accidentally overriding `sum` breaks all summation code.
 
**Example:**
```python
sum = 10  # Avoid this!
 
print(sum([1, 2, 3]))  # TypeError!
```
 
---
 
### 24. **What is the `map()` function used for?**  
**Answer:**  
`map()` applies a given function to each item of an iterable and returns a map object (lazy iterator).
 
**Scenario:**  
Convert all elements of a list to uppercase.
 
**Example:**
```python
names = ["ram", "raj"]
result = map(str.upper, names)
print(list(result))  # ['RAM', 'RAJ']
```
 
---
 
### 25. **How does `filter()` work in Python?**  
**Answer:**  
`filter()` returns items from an iterable for which the function returns `True`.
 
**Scenario:**  
Filter even numbers from a list.
 
**Example:**
```python
nums = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))  # [2, 4]
```
 
---
 
### 26. **Explain the use of `zip()`, `enumerate()`, and `all()` functions.**  
**Answer:**  
- `zip()`: Combines multiple iterables element-wise.  
- `enumerate()`: Returns index and value pairs.  
- `all()`: Returns `True` if all values are truthy.
 
**Scenario:**  
Work with pairs, indexed loops, or validation checks.
 
**Example:**
```python
names = ["A", "B"]
scores = [90, 80]
print(list(zip(names, scores)))  # [('A', 90), ('B', 80)]
 
for i, val in enumerate(["x", "y"]):
    print(i, val)
 
print(all([1, True, 5]))  # True
```
 
---
 
### 27. **What’s the difference between `any()` and `all()`?**  
**Answer:**  
- `any()`: Returns `True` if **at least one** value is truthy  
- `all()`: Returns `True` if **all** values are truthy
 
**Scenario:**  
Check if at least one user is online or if all users passed.
 
**Example:**
```python
print(any([False, True, False]))  # True
print(all([True, True, True]))    # True
```
 
---
 
### 28. **How can you use `eval()` function safely or what are the risks?**  
**Answer:**  
`eval()` executes a string as Python code. It's **dangerous** if used with untrusted input, as it can run malicious code.
 
**Scenario:**  
Calculate a string-based math expression **only if input is safe**.
 
**Example:**
```python
expr = "2 + 3 * 4"
print(eval(expr))  # 14
 
# Avoid: eval(input()) from users
```
 
---
 
### 29. **When would you use `id()`, `type()`, or `isinstance()` in real code?**  
**Answer:**  
- `id()`: Get memory address  
- `type()`: Check exact type  
- `isinstance()`: Check type including inheritance (recommended)
 
**Scenario:**  
Validate argument types in a function.
 
**Example:**
```python
x = 10
print(id(x))
print(type(x))
print(isinstance(x, int))  # True
```
 
---
 
### 30. **What are the most common built-in functions you use in Python projects?**  
**Answer:**  
Common ones include:
- `len()`, `sum()`, `max()`, `min()`, `sorted()`
- `type()`, `range()`, `enumerate()`, `zip()`, `map()`, `filter()`
- `any()`, `all()`, `input()`, `print()`
 
**Scenario:**  
Used in loops, data transformation, and input/output logic.
 
**Example:**
```python
numbers = [4, 2, 9]
print(sorted(numbers))     # [2, 4, 9]
print(sum(numbers))        # 15
print(len(numbers))        # 3
```
 
---