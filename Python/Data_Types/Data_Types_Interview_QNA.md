# Python Data Types – Comprehensive Q&A Guide
 
---
 
### **A. What are the different built-in data types in Python?**
 
**Answer:**  
Python has several built-in data types categorized as:
 
- **Numeric Types:** `int`, `float`, `complex`
- **Text Type:** `str`
- **Sequence Types:** `list`, `tuple`, `range`
- **Set Types:** `set`, `frozenset`
- **Mapping Type:** `dict`
- **Boolean Type:** `bool`
- **Binary Types:** `bytes`, `bytearray`, `memoryview`
- **None Type:** `NoneType`
 
---
 
### **B. What is the difference between mutable and immutable data types?**
 
**Answer:**  
- **Mutable:** Can be changed after creation (e.g., `list`, `dict`, `set`)
- **Immutable:** Cannot be changed after creation (e.g., `int`, `float`, `tuple`, `str`)
 
**Scenario Example:**  
In a game, scores (int) shouldn't change accidentally, but player inventory (list) can change.
 
```python
score = 100          # Immutable
inventory = ['sword', 'shield']  # Mutable
inventory.append('potion')
```

---
 
### **C. How does Python internally store different data types?**
 
**Answer:**  
Python uses objects for everything. Each data type is a class object under the hood.
 
- `int` is stored as a variable-length object in memory.
- `float` uses C `double` (64-bit).
- `list` and `dict` store references (pointers) to elements.
 

### **D. What is the default data type when we enter a number like `5.0` or `'5'`?**
 
**Answer:**
 
- `5.0` → `float`
- `'5'` → `str`
 
```python
type(5.0)    # <class 'float'>
type('5')    # <class 'str'>
```

### E. What are the differences between list, tuple, set, and dictionary?
 
| Type  | Ordered | Mutable | Duplicates | Indexed | Syntax         |
|-------|---------|---------|------------|---------|----------------|
| list  | Yes     | Yes     | Yes        | Yes     | `[1, 2, 3]`     |
| tuple | Yes     | No      | Yes        | Yes     | `(1, 2, 3)`     |
| set   | No      | Yes     | No         | No      | `{1, 2, 3}`     |
| dict  | Yes     | Yes     | Keys - No  | Keys    | `{'a': 1}`      |
 
---
 
### F. What is the use of the `frozenset` data type?
 
A `frozenset` is an **immutable set**. It is hashable and can be used as a dictionary key or inside other sets.
 
```python
fs = frozenset([1, 2, 3])
my_dict = {fs: "immutable set"}
```

### G. How is a generator different from a list in terms of memory?
`Generators` generate items on the fly using yield, so they are memory-efficient. Lists store all items in memory.
 
```python
def gen():
    for i in range(1000):
        yield i
g = gen()                      # Generator (lazy evaluation)
l = [i for i in range(1000)]   # List (eager evaluation)
```

### H. What is NoneType, and when do we use it?
`NoneType` represents the absence of a value. It is the type of the special constant None. Often used as a default return value or placeholder.
 
```python
def greet():
    print("Hi")
 
result = greet()       # prints Hi, returns None
print(type(result))    # <class 'NoneType'>
```

### I. What is the difference between int, float, and complex data types?
#### Type Example Description
- int 5 Whole numbers
- float 5.0 Numbers with decimal points
- complex 5 + 3j Numbers with imaginary part
 
```python
x = 5       # int
y = 5.0     # float
z = 5 + 3j  # complex
```

### J. How does Python support dynamic typing with respect to data types?
Python uses `dynamic typing`, which means you don’t declare variable types. The type is determined at runtime.
 
```python
x = 10        # int
x = "hello"   # now str
```

### K. How do you typecast one data type to another?
Use built-in functions like int(), float(), str() to convert between types.
 
```python
age = int(input("Enter your age: "))  # Convert string input to int
price = float("99.99")                # Convert string to float
```

### L. What is the difference between len() and __len__()?
len() is a built-in function.
 
Internally, it calls the object's __len__() method.
 
Prefer using len().
 
```python
l = [1, 2, 3]
print(len(l))        # 3
print(l.__len__())   # 3
```

### M. Explain memory allocation of immutable data types like int and str.
Python caches small immutable objects for efficiency (e.g., integers from -5 to 256). Reassigning creates new objects.
 
```python
a = 10
b = 10
print(id(a) == id(b))  # True (same memory reference)
 
a = 300
b = 300
print(id(a) == id(b))  # False (different objects)
```

### N. Why is a set unordered but a list is ordered?
List maintains order because it stores items by index.
 
Set is unordered because it uses a hash table for fast lookup, where order is not preserved.
 
```python
my_list = [1, 2, 3]
my_set = {3, 1, 2}
 
print(my_list)  # [1, 2, 3]
print(my_set)   # Output may be {1, 2, 3} or any order
```

## O. What is the difference between `is` and `==` in Python?
### 📌 Explanation:
- `==` checks for **value equality** — whether the values of two variables are the same.
- `is` checks for **identity** — whether two variables point to the same object in memory.
 
### 💡 Real-time Example:
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == c)  # True (same content)
print(a is c)  # False (different memory location)
print(a is b)  # True (same object)
```

### P. What is the difference between is, ==, and in?
**Operator Meaning Example**
- is Identity (same object in memory) a is b
- == Value equality a == b
- in Membership check 'a' in ['a', 'b', 'c'] → True
 
### Q. What is a ternary operator in Python?
📌 Explanation:
A ternary operator is a shorthand way of writing if-else in one line.
 
🔢 Syntax:

value_if_true if condition else value_if_false

💡 Example:
```python
x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)  # Output: Odd
```

### R. What is the use of the pass statement in Python?
📌 Explanation:
The pass statement is a placeholder. It does nothing but is used to maintain code structure where code is syntactically required.
 
💡 Example:
```python
for i in range(5):
    pass  # TODO: logic to be implemented later
```

### S. What are escape characters in Python?
📌 Explanation:
Escape characters are used to insert characters that are illegal in a string.
 
**Escape Sequence Meaning**
- \n Newline
- \t Tab
- \\ Backslash
- \' Single quote
- \" Double quote
 
💡 Example:
```python
print("Hello\nWorld")  # Output: Hello (newline) World
```

### T. What is string slicing in Python?
📌 Explanation:
Slicing is used to access parts of a string using index ranges.
 
🔢 Syntax:
python
string[start:stop:step]

💡 Example:
```python
text = "Python"
print(text[1:4])     # yth
print(text[::-1])    # Reverse the string: nohtyP
```

### U. What is the difference between len() and __len__()?
📌 Explanation:
len(obj) calls the built-in function.
 
__len__() is the special method inside the object that actually defines how length is calculated.
 
💡 Example:
```python
a = [1, 2, 3]
print(len(a))         # 3
print(a.__len__())    # 3
```

### V. What is type casting in Python?
📌 Explanation:
Type casting converts one data type to another.
 
🔢 Example:
```python
a = "123"
b = int(a)      # Converts string to integer
print(b + 1)    # Output: 124
```

### W. What is the use of format() function in strings?
📌 Explanation:
format() is used to insert values into strings using placeholders {}.
 
💡 Example:
```python
name = "Ganesh"
age = 22
print("My name is {} and I'm {} years old".format(name, age))
```

### X. What is a docstring in Python?
📌 Explanation:
A docstring is a multi-line string used to document functions, classes, or modules.
 
💡 Example:
```python
def add(a, b):
    """
    This function adds two numbers.
    """
    return a + b
 
print(add.__doc__)  # Prints the docstring
```

### Y. What is the use of comments in Python?
📌 Explanation:
Comments are used to explain code and are ignored during execution.
 
🔢 Syntax:
```python
# This is a single-line comment
```

### Z. How can you take input from the user in Python?
📌 Explanation:
Use input() to take user input (always returns a string).
 
💡 Example:
```python

name = input("Enter your name: ")
print("Hello", name)
```

----