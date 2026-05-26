# Python Loops – Practical Coding & Explanation-Based Questions
 
## 🔹 Basic to Intermediate – Coding
 
1. Write a Python program to print numbers from 1 to 10 using a loop.  
    ### Print numbers from 1 to 10
    ```python
    for i in range(1, 11):
        print(i)
    ```
    **Output:**
    ```
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    ```
---
2. Write a Python program to print even numbers between 1 and 20. 
    ### Print even numbers between 1 and 20
    ```python
    for i in range(2, 21, 2):
        print(i)
    ```
    **Output:**
    ```
    2
    4
    6
    8
    10
    12
    14
    16
    18
    20
    ```
---
3. Write a program to calculate the sum of numbers in a list using a `for` loop.
    ### Sum of numbers in a list
    ```python
    numbers = [1, 2, 3, 4, 5]
    total = 0
    for num in numbers:
        total += num
    print(total)
    ```
    **Output:**
    ```
    15
    ```    
---  
4. Write a program to count the number of vowels in a given string using a loop.
    ### Count vowels in a string
    ```python
    text = "interview"
    vowels = "aeiou"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    print(count)
    ```
    **Output:**
    ```
    3
    ```    
---  
5. Write a loop to print the multiplication table of a given number.
    ### Multiplication table of a number
    ```python
    num = 5
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    ```
    **Output:**
    ```
    5 x 1 = 5
    5 x 2 = 10
    ...
    5 x 10 = 50
    ```
---  
6. Write a Python program to reverse a string using a loop. 
    ### Reverse a string using loop
    ```python
    text = "python"
    reversed_text = ""
    for ch in text:
        reversed_text = ch + reversed_text
    print(reversed_text)
    ```
    **Output:**
    ```
    nohtyp
    ```
--- 
7. Write a loop to find the maximum element in a list (without using `max()`). 
    ### Find max element in a list
    ```python
    lst = [3, 8, 2, 7, 9]
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    print(max_val)
    ```
    **Output:**
    ```
    9
    ```
--- 
8. Write a program to print all prime numbers from 1 to 50 using a loop.
    ### Print prime numbers from 1 to 50
    ```python
    for num in range(2, 51):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
    ```
    **Output:**
    ```
    2
    3
    5
    7
    11
    13
    ...
    47
    ``` 
---  
9. Write a loop that skips printing when the number is divisible by 3.
    ### Skip numbers divisible by 3
    ```python
    for i in range(1, 11):
        if i % 3 == 0:
            continue
        print(i)
    ```
    **Output:**
    ```
    1
    2
    4
    5
    7
    8
    10
    ```
---  
10. Use a loop to display numbers from a list until a negative number is encountered.
    ### Display numbers until negative found
    ```python
    nums = [5, 3, 7, -1, 9]
    for num in nums:
        if num < 0:
            break
        print(num)
    ```
    **Output:**
    ```
    5
    3
    7
    ```
---  
 
## 🔹 Intermediate to Advanced – Coding
 
11. Write a nested loop to print a pattern (e.g., pyramid or square of stars).
    ### Print pattern of stars
    ```python
    for i in range(1, 6):
        print("*" * i)
    ```
    **Output:**
    ```
    *
    **
    ***
    ****
    *****
    ```
---
12. Write a program to flatten a 2D list using loops. 
    ### Flatten a 2D list
    ```python
    matrix = [[1, 2], [3, 4], [5, 6]]
    flat = []
    for row in matrix:
        for item in row:
            flat.append(item)
    print(flat)
    ```
    **Output:**
    ```
    [1, 2, 3, 4, 5, 6]
    ```    
--- 
13. Write a program using `for-else` that checks if a number exists in a list.
    ### Check if number exists using for-else
    ```python
    nums = [1, 3, 5, 7]
    target = 5
    for num in nums:
        if num == target:
            print("Found")
            break
    else:
        print("Not found")
    ```
    **Output:**
    ```
    Found
    ```
---
14. Implement a loop that executes for a specific duration using the `time` module.
    ### Loop runs for specific duration
    ```python
    import time
    start = time.time()
    while time.time() - start < 3:
        print("Running...")
        time.sleep(1)
    ```
    **Output:**
    ```
    Running...
    Running...
    Running...
    ```
---  
15. Create a loop using `enumerate()` to display item index and value.
    ### Use enumerate in loop
    ```python
    items = ['a', 'b', 'c']
    for index, value in enumerate(items):
        print(index, value)
    ```
    **Output:**
    ```
    0 a
    1 b
    2 c
    ``` 
---  
16. Create a loop using `zip()` to iterate over two lists at the same time.
    ### Use zip to iterate over lists
    ```python
    names = ['John', 'Jane']
    ages = [25, 30]
    for name, age in zip(names, ages):
        print(name, age)
    ```
    **Output:**
    ```
    John 25
    Jane 30
    ```
---
   
17. Simulate a simple loading animation using a loop and `time.sleep()`. 
    ### Loading animation simulation
    ```python
    import time
    for i in range(3):
        print("Loading.")
        time.sleep(0.5)
        print("Loading..")
        time.sleep(0.5)
        print("Loading...")
        time.sleep(0.5)
    ``` 
--- 
18. Write a program that prints the Fibonacci sequence using a loop.
    ### Fibonacci series using loop
    ```python
    a, b = 0, 1
    for _ in range(10):
        print(a)
        a, b = b, a + b
    ```
    **Output:**
    ```
    0
    1
    1
    2
    3
    5
    8
    13
    21
    34
    ```  
---
19. Detect and print duplicate elements in a list using loops. 
    ### Print duplicate elements in list
    ```python
    nums = [1, 2, 3, 2, 4, 1]
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    print(duplicates)
    ```
    **Output:**
    ```
    {1, 2}
    ```
--- 
20. Write a program that accepts user input until 'exit' is typed, using a loop.
    ### Accept input until 'exit' is typed
    ```python
    while True:
        user_input = input("Enter: ")
        if user_input.lower() == 'exit':
            break
        print("You typed:", user_input)
    ```
    **Output (example):**
    ```
    Enter: hello
    You typed: hello
    Enter: exit
    ```  
---
 
## 🔹 Interview-Specific Challenges – Code + Explain
    
21. Explain the output of a loop that uses both `break` and `continue`.
    ### Loop with break and continue
    ```python
    for i in range(5):
        if i == 2:
            continue
        if i == 4:
            break
        print(i)
    ```
    **Output:**
    ```
    0
    1
    3
    ```
---  
22. Analyze and explain a loop that modifies a list during iteration.
    ### Modify list during iteration (dangerous)
    ```python
    nums = [1, 2, 3, 4]
    for num in nums:
        if num % 2 == 0:
            nums.remove(num)
    print(nums)
    ```
    **Output:**
    ```
    [1, 3]
    ```
    > Not safe — always iterate over a copy when modifying. 
---  
23. Given a code snippet with nested loops, find its time complexity.
    ### Time complexity of nested loops
    ```python
    for i in range(3):
        for j in range(3):
            print(i, j)
    ```
    **Output:**
    ```
    0 0
    0 1
    0 2
    ...
    2 2
    ```
    **Time Complexity:** O(n²)
---  
24. Explain how an infinite loop can occur in `while` and how to avoid it.
    ### Avoid infinite loop in while
    ```python
    x = 5
    while x > 0:
        print(x)
        x -= 1
    ```
    **Output:**
    ```
    5
    4
    3
    2
    1
    ```
---  
25. Identify the bug in a loop that’s meant to remove elements from a list.
    ### Bug in removing elements from list
    ```python
    lst = [1, 2, 3, 4, 5]
    for i in lst:
        if i % 2 == 0:
            lst.remove(i)
    print(lst)
    ```
    **Output:**
    ```
    [1, 3, 5]
    ```
---  
26. Write a loop that sums digits of an integer (e.g., input: 123, output: 6).
    ### Sum digits of an integer
    ```python
    num = 123
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    print(total)
    ```
    **Output:**
    ```
    6
    ```
---  
27. Optimize a loop that filters odd numbers into a new list.
    ### Filter odd numbers into a new list
    ```python
    nums = [1, 2, 3, 4, 5]
    odds = []
    for num in nums:
        if num % 2 != 0:
            odds.append(num)
    print(odds)
    ```
    **Output:**
    ```
    [1, 3, 5]
    ```
--- 
28. Write a loop that finds the longest word in a sentence.
    ### Find longest word in sentence
    ```python
    sentence = "I love programming in Python"
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    print(longest)
    ```
    **Output:**
    ```
    programming
    ```    
---  
29. Implement a loop using a custom iterable class with `__iter__()` and `__next__()`.
    ### Custom iterable with __iter__ and __next__
    ```python
    class CountUp:
        def __init__(self, max):
            self.max = max
            self.num = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.num >= self.max:
                raise StopIteration
            self.num += 1
            return self.num
    
    for i in CountUp(5):
        print(i)
    ```
    **Output:**
    ```
    1
    2
    3
    4
    5
    ```
---  
30. Write a loop-based program to check if a string is a palindrome (without slicing).
    ### Check if string is palindrome using loop
    ```python
    text = "madam"
    rev = ""
    for ch in text:
        rev = ch + rev
    if text == rev:
        print("Palindrome")
    else:
        print("Not a palindrome")
    ```
    **Output:**
    ```
    Palindrome
    ```   
---
 
 