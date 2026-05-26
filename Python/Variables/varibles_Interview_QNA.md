## 📘 Basic-Level Interview Questions
 
---
 
### 1. What is a variable in Python?
 
A **variable** is a name that refers to a **value stored in memory**. It acts as a container to store data which can be used and modified later.
 
---
 
### 2. How do you declare a variable in Python?
 
You simply assign a value using the `=` operator. Python doesn't require declaring the type explicitly.
 
```python
x = 10
name = "Alice"
price = 99.99
```
---
## 3. What are the rules for naming variables in Python?
### ✅ Valid rules:
 
Must begin with a letter (a–z, A–Z) or an underscore (_)
 
Can contain letters, digits (0–9), and underscores
 
Cannot start with a digit
 
Cannot use reserved keywords (if, class, True, etc.)
 
```python
_name = "Ganesh"   # Valid
1var = 5           # Invalid
class = "Hello"    # Invalid (keyword)
```
---
## 4. What is dynamic typing in Python?
In Python, the type of a variable is determined at runtime and can be changed later.
 
```python
x = 10      # int
x = "Ten"   # str
```
---
## 5. Can you assign multiple values to multiple variables in one line? Explain with an example.
Yes, Python supports multiple assignment.
 
```python
a, b, c = 1, 2, 3
print(a, b, c)  # Output: 1 2 3
```
---
## 6. What happens if you assign a value to the same variable multiple times?
The latest value overrides the previous ones.
 
```python
x = 5
x = 10
print(x)  # Output: 10
```
---
## 7. What is the difference between a variable name and a value?
Variable name: Identifier that refers to a value (e.g., x)
 
Value: Actual data stored in memory (e.g., 10)
 
```python
x = 10  # x is the variable, 10 is the value
```
---
## 8. How can you swap two variable values in Python without using a temporary variable?
Use tuple unpacking:
 
```python
a = 5
b = 10
a, b = b, a
print(a, b)  # Output: 10 5
```
---
## 9. What are the standard conventions (PEP8) for writing variable names?
Use lowercase letters
 
Separate words with underscores (snake_case)
 
Use meaningful names
 
```python
user_name = "ganesh"
max_score = 100
```
---
## 10. What is variable unpacking? Give an example.
Variable unpacking means assigning elements of a sequence (list, tuple) to variables in one line.
 
```python
data = (1, 2, 3)
x, y, z = data
print(x, y, z)  # Output: 1 2 3
```
----

### 11. What is the difference between local and global variables?
 
- **Local Variable**: Defined inside a function and accessible only within it.
- **Global Variable**: Defined outside all functions and accessible throughout the module.
 
```python
x = "global"
 
def func():
    x = "local"
    print(x)
 
func()         # local
print(x)       # global
```

## 12. How does Python handle variable scope inside functions?
Python follows the LEGB Rule:
 
Local → inside current function
 
Enclosing → any enclosing functions
 
Global → module-level
 
Built-in → Python keywords/functions
 
```python
def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)
    
    inner()
 
outer()  # local
```
---
## 13. What is the use of the global keyword? Give an example.
Used to modify a global variable from inside a function.
 
```python
count = 0
 
def increment():
    global count
    count += 1
 
increment()
print(count)  # 1
```
---
## 14. What is the use of the nonlocal keyword? Give an example.
Used to modify a variable in the enclosing (non-global) scope.
 
```python
def outer():
    x = "outer"
    
    def inner():
        nonlocal x
        x = "modified"
    
    inner()
    print(x)
 
outer()  # Output: modified
```
---
## 15. How does variable shadowing work in Python?
When a local variable in a function has the same name as a global variable, it shadows the global variable.
 
```python
x = 10
 
def show():
    x = 20  # shadows the global x
    print(x)
 
show()     # 20
print(x)   # 10
```
---
## 16. How is memory management handled for variables in Python?
### Python uses:
 
Automatic memory management
 
Reference counting
 
Garbage collection
 
Unused or out-of-scope variables are automatically cleaned.
 
## 17. What is the difference between mutable and immutable variables? Give examples.
Mutable: Can be changed after creation (e.g., list, dict)
 
Immutable: Cannot be changed (e.g., int, str, tuple)
 
```python
# Mutable
a = [1, 2]
a.append(3)
print(a)  # [1, 2, 3]
 
# Immutable
x = "hello"
x = x + " world"
print(x)  # "hello world"
```
---
## 18. Explain how Python references variables in memory.
Variables store references (pointers) to objects in memory.
 
Multiple variables can refer to the same object.
 
```python
a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3] — both point to the same list
```
---
## 19. Can variables have the same name in different functions?
Yes. Each function has its own local scope, so the same variable name won't conflict.
 
```python
def func1():
    x = 5
    print(x)
 
def func2():
    x = 10
    print(x)
 
func1()  # 5
func2()  # 10
```
---
## 20. What happens when a variable is used before it is assigned?
It raises an error: UnboundLocalError or NameError.
 
```python
def test():
    print(x)  # Error
    x = 5
 
test()  # UnboundLocalError: local variable 'x' referenced before assignment
```
----

## 🚀 Advanced-Level Interview Questions with Answers, Real-Time Scenarios, and Code Examples
 
### 21. What is the difference between `is` and `==` in the context of variables?
 
* `==` checks for **value equality**.
* `is` checks for **identity (same memory location)**.
 
**Code Example:**
 
```python
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True
print(x is y)  # False
```
 
**Real-Time Scenario:**
When comparing user input with predefined config lists, use `==` instead of `is` to avoid logical bugs.
 
---
 
### 22. How does Python manage reference counting for variables?
 
Python keeps a count of how many references point to an object. When the count drops to 0, memory is freed.
 
**Code Example:**
 
```python
import sys
x = [1, 2, 3]
print(sys.getrefcount(x))
```
 
---
 
### 23. How does the garbage collector interact with variables?
 
Python’s garbage collector handles cyclic references—objects that refer to each other.
 
**Code Example:**
 
```python
import gc
gc.collect()  # Triggers garbage collection
```
 
**Real-Time Scenario:**
In long-running servers, calling `gc.collect()` manually during low traffic times can manage memory better.
 
---
 
### 24. Can you explain variable annotations in Python 3.6+? Give an example.
 
Used to specify variable types for readability and tools.
 
**Code Example:**
 
```python
name: str = "Gowri"
age: int = 22
```
 
---
 
### 25. What is type hinting and how is it useful in client-facing projects?
 
Type hinting helps with error checking, code completion, and documentation.
 
**Code Example:**
 
```python
def greet(name: str) -> str:
    return f"Hello {name}"
```
 
**Real-Time Scenario:**
Used in APIs to prevent type errors in data sent from the front end.
 
---
 
### 26. What is a closure and how do variables behave in closures?
 
A closure remembers the value from its enclosing scope.
 
**Code Example:**
 
```python
def outer():
    msg = "Hi"
    def inner():
        print(msg)
    return inner
f = outer()
f()
```
 
---
 
### 27. How do variables work in list comprehensions and generator expressions?
 
They have their own local scope in Python 3+.
 
**Code Example:**
 
```python
squares = [x*x for x in range(5)]
print(x)  # NameError in Python 3
```
 
---
 
### 28. What is a namespace? How does Python handle variable resolution in namespaces?
 
Namespace is a mapping from names to objects.
 
**Real-Time Scenario:**
Global, local, and built-in variables exist in different namespaces.
 
**Code Example:**
 
```python
def func():
    x = 10
    print(locals())
func()
```
 
---
 
### 29. Explain the LEGB rule in Python with an example.
 
LEGB: Local → Enclosing → Global → Built-in.
 
**Code Example:**
 
```python
def outer():
    x = 'enclosing'
    def inner():
        print(x)
    inner()
outer()
```
 
---
 
### 30. Can you use a variable as a function name? What are the implications?
 
Yes, but it overrides the original function.
 
**Code Example:**
 
```python
print = 5
print("Hi")  # TypeError
```
 
**Tip:** Avoid naming variables after built-ins.
 
---
 
### 31. What is the difference between shallow and deep copying with variables?
 
* Shallow copy: One-level copy.
* Deep copy: Full independent copy.
 
**Code Example:**
 
```python
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
```
 
---
 
### 32. How do class variables differ from instance variables?
 
* Class vars shared across instances.
* Instance vars are specific to one object.
 
**Code Example:**
 
```python
class Student:
    school = "XYZ"  # Class variable
    def __init__(self, name):
self.name = name  # Instance variable
```
 
---
 
### 33. How can environment variables be accessed and used in Python?
 
**Code Example:**
 
```python
import os
os.environ['API_KEY'] = 'abc123'
print(os.getenv('API_KEY'))
```
 
**Real-Time Scenario:**
Used to store secrets like API keys or DB passwords.
 
---
 
### 34. What are some real-time examples of bugs caused due to improper variable handling?
 
* Reusing loop variables outside the loop.
* Shadowing built-in functions like `list`, `str`, etc.
 
**Example:**
 
```python
str = "hello"
print(str(123))  # TypeError
```
 
---
 
### 35. How does the `id()` function help in debugging variable behavior?
 
It returns the memory address. Helps identify if variables point to the same object.
 
**Code Example:**
 
```python
a = [1, 2]
b = a
print(id(a), id(b))  # Same IDs
```