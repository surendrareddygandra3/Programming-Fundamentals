# 📘 Python Variables
 
## 🔹 What is a Variable?
 
A **variable** in Python is a **name** that refers to a **value stored in memory**. It acts as a container for data that can be used and modified later.
 
---
 
## 🔹 Variable Declaration & Assignment
 
```python
x = 10         # Integer
name = "Alice" # String
price = 99.99  # Float
```
No need to declare the type.
 
Python is dynamically typed, so variable types are inferred at runtime.
 
## 🔹 Rules for Naming Variables
✅ Valid:
 
Must start with a letter or underscore _
 
Can contain letters, numbers, and underscores
 
❌ Invalid:
 
Cannot start with a number
 
Cannot use Python keywords (if, for, class, etc.)
 
```python
_age = 25     # Valid
2price = 10   # ❌ Invalid
class = "A"   # ❌ Invalid
```

## 🔹 Variable Types (Implicit Typing)
Python automatically assigns a data type based on the value.
 
```python
a = 5         # int
b = 5.5       # float
c = "Hello"   # str
d = True      # bool
```
Use type() to check the type:
 
```python
print(type(a))  # <class 'int'>
```
## 🔹 Dynamic Typing
Variables can be reassigned to different types:
 
```python
x = 10
x = "Ten"
```
## 🔹 Multiple Assignment
```python
x, y, z = 1, 2, 3       # Assign different values
a = b = c = 100         # Assign same value
```
## 🔹 Real-Time Scenario
E-commerce Checkout:
 
```python
item_price = 250.75
quantity = 3
total_cost = item_price * quantity
print("Total:", total_cost)
```
## 🔹 Constants in Python
By convention, constants are named in UPPERCASE, but Python doesn't enforce it:
 
```python
PI = 3.14159
MAX_USERS = 100
```
## 🔹 Global vs Local Variables
```python
x = 50  # Global
 
def my_func():
    x = 10  # Local
    print("Inside:", x)
 
my_func()
print("Outside:", x)
```
## 🔹 global Keyword
Used to modify a global variable inside a function:
 
```python
count = 0
 
def increment():
    global count
    count += 1
```
## 🔹 del Keyword
Used to delete a variable:
 
```python
x = 5
del x
# print(x) → NameError
```
## 🔹 Best Practices
### ✅ Use meaningful variable names
### ✅ Follow snake_case naming style
### ✅ Avoid single-letter names (except in loops)
### ✅ Use constants for fixed values
 
### ✅ Summary
|Feature	|Description|
|-----------|-----------|
|Dynamic Typing |Type changes with assigned value|
|Multiple Assignment|Assign multiple values at once|
|type() |Check variable type|
|global / local	 | Scope of variables|
|del |Delete a variable
 



