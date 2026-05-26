# Python Conditional Statements – Coding Questions with Answers
 
## ✅ Basic-Level Coding Questions (1–10)
 
---
 
### 1. Check if a number is positive or negative
```python
num = -5
if num >= 0:
    print("Positive")
else:
    print("Negative")
```
**Output:**
```
Negative
```
 
---
 
### 2. Check if a number is even or odd
```python
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```
**Output:**
```
Even
```
 
---
 
### 3. Find the greatest of two numbers
```python
a, b = 15, 25
if a > b:
    print(a)
else:
    print(b)
```
**Output:**
```
25
```
 
---
 
### 4. Check if a number is in a given range (1 to 100)
```python
num = 55
if 1 <= num <= 100:
    print("In range")
else:
    print("Out of range")
```
**Output:**
```
In range
```
 
---
 
### 5. Check if a character is a vowel
```python
ch = 'e'
if ch.lower() in 'aeiou':
    print("Vowel")
else:
    print("Consonant")
```
**Output:**
```
Vowel
```
 
---
 
### 6. Use `if-elif-else` to assign grades
```python
marks = 78
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")
```
**Output:**
```
B
```
 
---
 
### 7. Check if a year is a leap year
```python
year = 2024
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
```
**Output:**
```
Leap year
```
 
---
 
### 8. Use ternary operator to print min of two numbers
```python
a, b = 10, 5
print(a if a < b else b)
```
**Output:**
```
5
```
 
---
 
### 9. Check if a number is divisible by both 3 and 5
```python
n = 15
if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both")
else:
    print("Not divisible")
```
**Output:**
```
Divisible by both
```
 
---
 
### 10. Check if input is empty
```python
user_input = ""
if not user_input:
    print("Input is empty")
```
**Output:**
```
Input is empty
```
 
---
 
## ✅ Intermediate-Level Coding Questions (11–20)
 
---
 
### 11. Find the largest of 3 numbers
```python
a, b, c = 10, 20, 15
if a >= b and a >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)
```
**Output:**
```
20
```
 
---
 
### 12. Nested `if` for age and eligibility
```python
age = 20
citizen = True
if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Underage")
```
**Output:**
```
Eligible to vote
```
 
---
 
### 13. Check if input is digit, alphabet or special character
```python
ch = '$'
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")
```
**Output:**
```
Special Character
```
 
---
 
### 14. Compare two strings ignoring case
```python
s1 = "Hello"
s2 = "hello"
if s1.lower() == s2.lower():
    print("Same")
else:
    print("Different")
```
**Output:**
```
Same
```
 
---
 
### 15. Check if a string is palindrome
```python
text = "madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
```
**Output:**
```
Palindrome
```
 
---
 
### 16. Use condition to format message
```python
logged_in = False
print("Welcome" if logged_in else "Please log in")
```
**Output:**
```
Please log in
```
 
---
 
### 17. Check password strength based on length
```python
password = "abc123"
if len(password) < 6:
    print("Weak")
elif len(password) < 10:
    print("Moderate")
else:
    print("Strong")
```
**Output:**
```
Moderate
```
 
---
 
### 18. Short-circuiting demo with `and`
```python
x = None
if x is not None and x > 0:
    print("Positive number")
else:
    print("Invalid or non-positive")
```
**Output:**
```
Invalid or non-positive
```
 
---
 
### 19. Truthy values in if statement
```python
val = []
if val:
    print("Has content")
else:
    print("Empty")
```
**Output:**
```
Empty
```
 
---
 
### 20. Multiple `elif` conditions
```python
x = 0
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```
**Output:**
```
Zero
```
 
---
 
## ✅ Advanced / Real-Life Scenario Based (21–30)
 
---
 
### 21. Use `if-else` with loop (Login attempts)
```python
password = "admin"
for i in range(3):
    attempt = input("Enter password: ")
    if attempt == password:
        print("Access granted")
        break
else:
    print("Access denied")
```
**Sample Output:**
```
Enter password: wrong
Enter password: admin
Access granted
```
 
---
 
### 22. Guard clause to exit early
```python
def process_age(age):
    if age < 0:
        return "Invalid age"
    if age < 18:
        return "Minor"
    return "Adult"
 
print(process_age(16))
```
**Output:**
```
Minor
```
 
---
 
### 23. Replace `if-elif` with dictionary
```python
operation = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y
}
print(operation.get('add', lambda x, y: "Invalid")(5, 3))
```
**Output:**
```
8
```
 
---
 
### 24. Day of week using `match-case` (Python 3.10+)
```python
day = 2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Other day")
```
**Output:**
```
Tuesday
```
 
---
 
### 25. Check if a year is century year
```python
year = 1900
if year % 100 == 0:
    print("Century year")
else:
    print("Not a century year")
```
**Output:**
```
Century year
```
 
---
 
### 26. Temperature alert system
```python
temp = 39
if temp > 40:
    print("High Fever")
elif temp >= 37:
    print("Mild Fever")
else:
    print("Normal")
```
**Output:**
```
Mild Fever
```
 
---
 
### 27. Validate user age and subscription
```python
age = 21
subscribed = True
if age >= 18 and subscribed:
    print("Access content")
else:
    print("Access denied")
```
**Output:**
```
Access content
```
 
---
 
### 28. Discount logic using nested conditionals
```python
price = 1500
member = True
if price > 1000:
    if member:
        print("20% Discount")
    else:
        print("10% Discount")
else:
    print("No Discount")
```
**Output:**
```
20% Discount
```
 
---
 
### 29. Detect triangle type based on sides
```python
a, b, c = 5, 5, 5
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
```
**Output:**
```
Equilateral
```
 
---
 
### 30. Role-based access control
```python
role = "admin"
if role == "admin":
    print("Full access")
elif role == "editor":
    print("Edit access")
else:
    print("View only")
```
**Output:**
```
Full access
```
 
---
 