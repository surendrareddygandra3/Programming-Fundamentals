# Python Interview Questions: Variables (Client-Focused)
 
This section covers **Python Variables** from basic to advanced, in **numbered format** for clarity and expansion, along with **code examples**.
 
---
 
## 📘 Basic-Level Interview Questions with Examples
 
1. **What is a variable in Python?**
   A variable is a name that refers to a value stored in memory.
 
   ```python
   x = 10
   name = "Ganesh"
   ```
 
2. **How do you declare a variable in Python?**
   Variables are declared by assigning a value using the `=` operator.
 
   ```python
   age = 25
   ```
 
3. **What are the rules for naming variables in Python?**
 
   * Must start with a letter or underscore
   * Cannot start with a digit
   * Can contain letters, digits, and underscores
   * Case-sensitive
 
4. **What is dynamic typing in Python?**
   You don’t need to declare variable types.
 
   ```python
   x = 5     # Integer
   x = "Hi"  # Now a string
   ```
 
5. **Can you assign multiple values to multiple variables in one line?**
 
   ```python
   a, b, c = 1, 2, 3
   ```
 
6. **What happens if you assign a value to the same variable multiple times?**
   The latest value will overwrite the previous one.
 
   ```python
   x = 10
   x = 20  # Now x is 20
   ```
 
7. **What is the difference between a variable name and a value?**
   The variable name is a reference to a memory location storing the value.
 
8. **How can you swap two variable values in Python without using a temporary variable?**
 
   ```python
   a, b = 5, 10
   a, b = b, a
   ```
 
9. **What are the standard conventions (PEP8) for writing variable names?**
   Use lowercase letters with underscores (e.g., `my_variable`).
 
10. **What is variable unpacking?**
 
```python
data = (1, 2, 3)
x, y, z = data
```
 
---
 
## 🧩 Intermediate-Level Interview Questions with Examples
 
11. **What is the difference between local and global variables?**
 
```python
x = 10  # Global
def func():
    y = 5  # Local
```
 
12. **How does Python handle variable scope inside functions?**
    It uses the LEGB rule (Local, Enclosing, Global, Built-in).
 
13. **What is the use of the `global` keyword?**
 
```python
x = 5
def change():
    global x
    x = 10
```
 
14. **What is the use of the `nonlocal` keyword?**
 
```python
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    print(x)
```
 
15. **How does variable shadowing work in Python?**
    A local variable can shadow a global variable with the same name.
 
16. **How is memory management handled for variables in Python?**
    Python uses reference counting and garbage collection.
 
17. **Difference between mutable and immutable variables:**
 
```python
# Immutable
x = 10
x = x + 1
 
# Mutable
my_list = [1, 2]
my_list.append(3)
```
 
18. **How does Python reference variables in memory?**
    Variables reference objects by storing memory addresses (pointers).
 
19. **Can variables have the same name in different functions?**
    Yes, because each function has its own local scope.
 
20. **What happens when a variable is used before it is assigned?**
    Python raises an `UnboundLocalError`.
 
```python
def test():
    print(x)
    x = 5  # Error: x used before assignment
```
 
---
 
## 🚀 Advanced-Level Interview Questions with Examples
 
21. **Difference between `is` and `==`:**
 
```python
a = [1, 2]
b = [1, 2]
print(a == b)  # True
print(a is b)  # False
```
 
22. **How does Python manage reference counting?**
    Python internally tracks how many references point to an object. When the count reaches zero, it’s deleted.
 
23. **How does the garbage collector interact with variables?**
    Python’s GC cleans up unused objects using reference counting and cyclic GC.
 
24. **Variable annotations in Python 3.6+:**
 
```python
name: str = "Ganesh"
age: int = 25
```
 
25. **What is type hinting?**
    Helps IDEs and developers understand variable types.
 
```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```
 
26. **What is a closure?**
 
```python
def outer():
    x = 10
    def inner():
        print(x)
    return inner
closure_func = outer()
closure_func()
```
 
27. **Variables in list comprehensions:**
 
```python
squares = [x*x for x in range(5)]
```
 
28. **What is a namespace?**
    It’s a container mapping names to objects. Examples: local, global, built-in.
 
29. **LEGB Rule:**
 
```python
def outer():
    x = "enclosing"
    def inner():
        print(x)
    inner()
```
 
30. **Can a variable be used as a function name?**
    Yes, but it will overwrite the function.
 
```python
def my_func():
    print("Hi")
my_func = 10  # Now 'my_func' is an int
```
 
31. **Shallow vs Deep Copying:**
 
```python
import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)      # Shallow copy
c = copy.deepcopy(a)  # Deep copy
```
 
32. **Class vs Instance Variables:**
 
```python
class Test:
    class_var = 10
    def __init__(self):
        self.instance_var = 20
```
 
33. **Accessing Environment Variables:**
 
```python
import os
os.getenv("HOME")
```
 
34. **Bugs from improper variable handling:**
 
* Using global variables inside functions unintentionally.
* Overwriting built-in names like `list`, `str`.
 
35. **Using `id()` for debugging:**
 
```python
x = [1, 2, 3]
print(id(x))
```
 
---