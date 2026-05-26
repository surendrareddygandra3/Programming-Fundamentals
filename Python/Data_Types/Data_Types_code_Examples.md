# Python Data Types: A to Z Interview Questions with Code Examples
 
## ✅ Basic Level
 
### A. What are the different built-in data types in Python?
 
```python
x = 10              # int
y = 3.14            # float
z = 1 + 2j          # complex
s = "Hello"         # str
l = [1, 2, 3]       # list
t = (1, 2, 3)       # tuple
se = {1, 2, 3}      # set
d = {"a": 1}        # dict
b = True            # bool
n = None            # NoneType
```
 
### B. What is the difference between mutable and immutable data types?
 
```python
# Immutable: cannot be changed after assignment
x = 10
x = 20  # New object is created
 
# Mutable: can be modified
l = [1, 2, 3]
l.append(4)  # modifies original list
```
 
### C. How does Python internally store different data types?
 
```python
x = 10
print(id(x))  # memory address
```
 
### D. What is the default data type when we enter a number like `5.0` or `"5"`?
 
```python
print(type(5.0))  # float
print(type("5"))  # str
```
 
### E. Differences between list, tuple, set, and dictionary:
 
```python
my_list = [1, 2, 3]        # Ordered, mutable
my_tuple = (1, 2, 3)       # Ordered, immutable
my_set = {1, 2, 3}         # Unordered, unique, mutable
my_dict = {"a": 1}        # Key-value, mutable
```
 
## ✅ Intermediate Level
 
### F. What is the use of the `frozenset` data type?
 
```python
fs = frozenset([1, 2, 3])  # Immutable version of a set
```
 
### G. How is a `generator` different from a `list`?
 
```python
def gen():
    yield 1
    yield 2
 
print(list(gen()))
```
 
### H. What is `NoneType`?
 
```python
def func():
    pass
 
print(func())  # Output: None
```
 
### I. Difference between `int`, `float`, and `complex`
 
```python
x = 10         # int
y = 10.5       # float
z = 2 + 3j     # complex
```
 
### J. How does Python support dynamic typing?
 
```python
x = 10
x = "Now a string"  # Valid
```
 
### K. Typecasting one type to another:
 
```python
x = "123"
num = int(x)  # str to int
```
 
### L. Difference between `len()` and `__len__()`:
 
```python
lst = [1, 2, 3]
print(len(lst))
print(lst.__len__())
```
 
### M. Memory allocation of immutable data types:
 
```python
x = 100
print(id(x))
x = 200
print(id(x))  # New memory location
```
 
### N. Why is a `set` unordered?
 
```python
my_set = {3, 2, 1}
print(my_set)  # Random order
```
 
### O. Relation of `object` and `type`:
 
```python
print(type(5))           # <class 'int'>
print(isinstance(5, object))  # True
```
 
## ✅ Advanced Level
 
### P. Precision in float:
 
```python
x = 1.12345678901234567890
print(x)  # Python supports ~15-17 digits of precision
```
 
### Q. What happens if you add different types?
 
```python
x = 5 + 2.0   # Valid: int + float -> float
# y = 5 + "2"  # Error: int + str
```
 
### R. Nested data types:
 
```python
nested = [{"a": [1, 2]}, {"b": (3, 4)}]
```
 
### S. Difference between `str` and `repr`:
 
```python
import datetime
now = datetime.datetime.now()
print(str(now))
print(repr(now))
```
 
### T. Tuple vs List:
 
```python
my_list = [1, 2]
my_tuple = (1, 2)
my_list[0] = 100  # Valid
# my_tuple[0] = 100  # Error
```
 
### U. `None` vs `NaN`:
 
```python
import math
x = None
y = float('nan')
print(x == None)       # True
print(math.isnan(y))   # True
```
 
### V. Variable declaration without type:
 
```python
x = 10
x = "Now string"
```
 
### W. Comparison between types:
 
```python
x = 5
y = "5"
# print(x == y)  # False
# print(x is y)  # False
```
 
### X. Dictionary key hashing:
 
```python
d = {"a": 1, 2: "b"}  # Only hashable types can be keys
```
 
### Y. Changing type after assignment:
 
```python
x = 100
x = "Now I'm a string"
```
 
### Z. User-defined data types:
 
```python
class Person:
    def __init__(self, name):
self.name = name
 
p = Person("Gowri")
print(p.name)
```