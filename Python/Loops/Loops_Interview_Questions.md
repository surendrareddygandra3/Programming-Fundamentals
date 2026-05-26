# Python Interview Questions – Loops (30 Questions)
 
## 🔹 Basic to Intermediate
 
### 1. What are the types of loops available in Python?  
**Answer:**  
    Python provides two main loops:
    - `for` loop: used for iterating over sequences like lists, strings, or tuples.
    - `while` loop: used to execute a block of code repeatedly as long as a condition is `True`.
    
**Scenario:**  
    Use `for` to process each order in a list; use `while` to retry a connection until it succeeds.
    
**Example:**
```
# for loop
orders = ['Order1', 'Order2']
for order in orders:
    print("Processing", order)
    
# while loop
attempts = 0
while attempts < 3:
    print("Trying to connect...")
    attempts += 1
```
    
---
 
### 2. How does the `for` loop work in Python?  
**Answer:**  
A `for` loop automatically iterates over any iterable (like list, string, or range) and processes each item. Internally, it uses the iterator protocol (`__iter__` and `__next__`).
 
**Scenario:**  
Sending a welcome message to every registered user in a list.
 
**Example:**
```python
users = ['Alice', 'Bob']
for user in users:
    print(f"Welcome, {user}!")
```
 
---
 
### 3. How does the `while` loop work in Python?  
**Answer:**  
A `while` loop runs repeatedly as long as a specified condition remains `True`. It's used when the number of iterations is unknown beforehand.
 
**Scenario:**  
Keep asking for user input until the correct password is entered.
 
**Example:**
```python
password = ''
while password != 'admin':
    password = input("Enter password: ")
print("Access granted")
```
 
---
 
### 4. What is the difference between `for` and `while` loops?  
**Answer:**  
- Use `for` when you know how many times to loop or when iterating over a collection.
- Use `while` when looping depends on a condition that might change during execution.
 
**Scenario:**  
`for` to print numbers from 1–10, `while` to keep asking a user until they agree.
 
**Example:**
```python
# for loop
for i in range(1, 11):
    print(i)
 
# while loop
response = ''
while response.lower() != 'yes':
    response = input("Do you accept the terms? ")
```
 
---
 
### 5. What is the purpose of the `range()` function in loops?  
**Answer:**  
`range()` generates a sequence of numbers and is commonly used in `for` loops to define how many times the loop should run.
 
**Scenario:**  
Send email reminders 5 times using a loop with `range()`.
 
**Example:**
```python
for i in range(5):
    print(f"Sending reminder {i + 1}")
```
 
---
 
### 6. How can you iterate over a dictionary using a loop?  
**Answer:**  
Use the `.items()` method with a `for` loop to access both keys and values.
 
**Scenario:**  
Display user details from a dictionary.
 
**Example:**
```python
user = {'name': 'John', 'age': 30}
for key, value in user.items():
    print(f"{key.capitalize()}: {value}")
```
 
---
 
### 7. What are `break`, `continue`, and `pass` statements?  
**Answer:**  
- `break`: Exits the loop immediately.
- `continue`: Skips the current iteration and continues with the next.
- `pass`: Does nothing; used as a placeholder when code is syntactically required.
 
**Scenario:**  
Exit loop when a match is found, skip invalid data, or leave a block for future use.
 
**Example:**
```python
for num in range(5):
    if num == 2:
        continue
    if num == 4:
        break
    print(num)
 
# Output: 0, 1, 3
```
 
---
 
### 8. How can you loop through both keys and values in a dictionary?  
**Answer:**  
Use `for key, value in dict.items()` to access both the key and its corresponding value in each iteration.
 
**Scenario:**  
Printing configuration settings from a dictionary.
 
**Example:**
```python
config = {'host': 'localhost', 'port': 8080}
for key, value in config.items():
    print(f"{key} -> {value}")
```
 
---
 
### 9. What is an infinite loop, and how can it be avoided?  
**Answer:**  
An infinite loop is a loop that never ends due to a condition that always remains `True`. It can be avoided by ensuring proper termination conditions or using `break`.
 
**Scenario:**  
Prompt user until they choose to exit — prevent infinite loop using a break.
 
**Example:**
```python
while True:
    cmd = input("Enter command (type 'exit' to stop): ")
    if cmd == 'exit':
        break
```
 
---
 
### 10. How can you use nested loops in Python?  
**Answer:**  
A nested loop is a loop inside another loop, useful for working with multidimensional data like matrices.
 
**Scenario:**  
Printing a multiplication table or processing a 2D list.
 
**Example:**
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=' ')
    print()
```
 
### 11. What does the `else` clause do in a loop?  
**Answer:**  
The `else` clause in a loop runs **only if the loop completes normally**, i.e., it does **not hit a `break`**.
 
**Scenario:**  
Search for an item in a list and report if not found.
 
**Example:**
```python
numbers = [1, 3, 5]
for num in numbers:
    if num == 4:
        print("Found")
        break
else:
    print("Not Found")  # runs if break not executed
```
 
---
 
### 12. How do you iterate over two or more sequences simultaneously?  
**Answer:**  
Use the `zip()` function to pair elements from multiple iterables.
 
**Scenario:**  
Combine student names and their scores into a report.
 
**Example:**
```python
names = ['Alice', 'Bob']
scores = [85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```
 
---
 
### 13. How can you reverse a loop iteration?  
**Answer:**  
Use the `reversed()` function or reverse the iterable before looping.
 
**Scenario:**  
Count down from 5 to 1.
 
**Example:**
```python
for i in reversed(range(1, 6)):
    print(i)
```
 
---
 
### 14. How can you skip even numbers using a loop?  
**Answer:**  
Use `continue` inside an `if` statement to skip even values.
 
**Scenario:**  
Only print odd numbers between 0 and 10.
 
**Example:**
```python
for i in range(11):
    if i % 2 == 0:
        continue
    print(i)  # prints 1, 3, 5, 7, 9
```
 
---
 
### 15. What is the time complexity of loops in Python?  
**Answer:**  
It depends on the structure:
- Single loop: O(n)
- Nested loop: O(n²) or higher depending on depth
 
**Scenario:**  
A nested loop iterating over a grid of size `n x n` has time complexity O(n²).
 
**Example:**
```python
for i in range(n):
    for j in range(n):
        print(i, j)  # O(n²)
```
 
---  
 
## 🔹 Advanced and Scenario-Based
 
### 16. Can a `for` loop be used with a custom iterable object?  
**Answer:**  
Yes. If an object implements the `__iter__()` method, it can be used in a `for` loop.
 
**Scenario:**  
Create a custom object that returns numbers 1 to 3 on iteration.
 
**Example:**
```python
class MyRange:
    def __iter__(self):
        return iter([1, 2, 3])
 
for num in MyRange():
    print(num)
```
 
---
 
### 17. What is the difference between `range()` and `xrange()`?  
**Answer:**  
- `range()` returns a list (Python 2) or a range object (Python 3)
- `xrange()` exists only in Python 2 and is more memory-efficient
 
**Scenario:**  
In Python 2, prefer `xrange()` for large ranges to save memory.
 
---
 
### 18. How do list comprehensions relate to loops?  
**Answer:**  
List comprehensions provide a compact way to write loops that create new lists.
 
**Scenario:**  
Generate a list of squares from 1 to 5 in one line.
 
**Example:**
```python
squares = [x*x for x in range(1, 6)]
```
 
---
 
### 19. Can you write a generator expression instead of a loop?  
**Answer:**  
Yes. Generator expressions are like list comprehensions but use lazy evaluation.
 
**Scenario:**  
Process large data line by line without loading it all into memory.
 
**Example:**
```python
gen = (x*x for x in range(1_000_000))
for val in gen:
    break  # stops after first value
```
 
---
 
### 20. How do you count the number of iterations in a loop?  
**Answer:**  
Use a manual counter or the built-in `enumerate()` function to track iteration count.
 
**Scenario:**  
Track student ranks while looping through their names.
 
**Example:**
```python
students = ['Alice', 'Bob']
for idx, name in enumerate(students, start=1):
    print(f"{idx}. {name}")
```
 
---
 
### 21. How can you write a loop that tracks both the index and value?  
**Answer:**  
Use `enumerate()` which returns both the index and the item from the iterable.
 
**Scenario:**  
Display index alongside elements in a menu.
 
**Example:**
```python
menu = ['Home', 'About', 'Contact']
for idx, item in enumerate(menu):
    print(f"{idx}: {item}")
```
 
---
 
### 22. How does `for-else` differ from `try-else`?  
**Answer:**  
- `for-else`: `else` executes only if the loop **does not hit a `break`**.  
- `try-else`: `else` executes only if **no exception** is raised.
 
**Scenario:**
```python
# for-else
for n in [1, 2, 3]:
    if n == 5:
        break
else:
    print("5 not found")
 
# try-else
try:
    x = 1 / 1
except ZeroDivisionError:
    print("Error")
else:
    print("No error occurred")
```
 
---
 
### 23. Can a loop be interrupted by exceptions?  
**Answer:**  
Yes. If an exception occurs during iteration, it breaks the loop unless handled with `try-except`.
 
**Scenario:**  
Handle division errors during a loop.
 
**Example:**
```python
for i in [2, 1, 0]:
    try:
        print(10 // i)
    except ZeroDivisionError:
        print("Cannot divide by zero")
```
 
---
 
### 24. Write a loop that checks if a list is a palindrome.  
**Answer:**  
Compare the list with its reverse using a loop or slicing.
 
**Scenario:**  
Check if the word list `['m', 'a', 'd', 'a', 'm']` is a palindrome.
 
**Example:**
```python
word = ['m', 'a', 'd', 'a', 'm']
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
```
 
---
 
### 25. How would you write a loop that runs for exactly 3 seconds?  
**Answer:**  
Use the `time` module to track how long the loop has been running.
 
**Scenario:**  
Perform heartbeat/polling for a fixed 3-second window.
 
**Example:**
```python
import time
start = time.time()
while time.time() - start < 3:
    print("Running...")
    time.sleep(1)
```
 
--- 
 
## 🔹 Optional Deep Dive / Advanced Concepts
 
# 🔁 Python Loops – Advanced Q&A (26–30 with Scenarios)
 
---
 
### 26. How do Python loops handle memory in large datasets?  
**Answer:**  
When looping over large datasets, Python is memory-efficient if **iterators or generators** are used instead of storing the entire data in memory.
 
**Scenario:**  
Reading a 10GB file line-by-line using a generator avoids memory overload.
 
**Example:**
```python
with open('large_file.txt') as file:
    for line in file:
        process(line)  # Efficient memory usage
```
 
---
 
### 27. What are iterators and how do they relate to loops?  
**Answer:**  
An iterator is an object with `__iter__()` and `__next__()` methods that allow you to fetch items one by one. `for` loops use iterators under the hood.
 
**Scenario:**  
Custom iterable object to return numbers one by one.
 
**Example:**
```python
class CountUp:
    def __init__(self, max):
        self.n = 1
        self.max = max
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= self.max:
            val = self.n
            self.n += 1
            return val
        raise StopIteration
 
for i in CountUp(3):
    print(i)
```
 
---
 
### 28. What’s the role of `__iter__()` and `__next__()` in looping mechanisms?  
**Answer:**  
- `__iter__()` returns the iterator object itself  
- `__next__()` returns the next value and raises `StopIteration` when done  
These methods make an object iterable in `for` loops.
 
**Scenario:**  
Creating your own class that works like `range`.
 
**Example:**
```python
class MyRange:
    def __init__(self, end):
        self.current = 0
        self.end = end
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.current < self.end:
            self.current += 1
            return self.current - 1
        raise StopIteration
 
for i in MyRange(3):
    print(i)
```
 
---
 
### 29. How does Python handle the Global Interpreter Lock (GIL) with loops in multithreading?  
**Answer:**  
The GIL prevents multiple threads from executing Python bytecode at the same time. In **CPU-bound loops**, threading won't improve performance. Use **multiprocessing** instead.
 
**Scenario:**  
Looping over a CPU-intensive calculation — prefer multiprocessing.
 
**Example:**
```python
# Bad with threading for CPU-bound tasks
from threading import Thread
 
# Better with multiprocessing
from multiprocessing import Process
```
 
---
 
### 30. Explain the difference between eager and lazy iteration in Python.  
**Answer:**  
- **Eager iteration**: all values are computed and stored in memory (e.g., lists)  
- **Lazy iteration**: values are generated one by one as needed (e.g., generators)
 
**Scenario:**  
Use a generator for large log processing to avoid memory issues.
 
**Example:**
```python
# Eager
nums = [x*x for x in range(1000000)]  # All stored
 
# Lazy
nums = (x*x for x in range(1000000))  # Generated on the fly
```
 
---
 