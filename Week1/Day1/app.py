# ==========================================

# Week 1 - Day 1

# Python Fundamentals Playground

# Purpose:

# Record concepts learned and execute examples

# ==========================================

# ------------------------------------------

# PRINT FUNCTION

# ------------------------------------------

print("Hello World")

# Multiplication with strings

print("*" * 10)

# ------------------------------------------

# LINTING (Code Quality)

# ------------------------------------------

# Uncomment below and observe linter warnings

# x =   10

# Linting checks:

# - spacing

# - style violations

# - possible bugs

# - readability

# VS Code:

# Ctrl + Shift + P

# → Search "Lint"

# → Select Configure Linting

# Optional:

# Settings

# → Format On Save = ON

# ------------------------------------------

# VARIABLES

# ------------------------------------------

name = "Tarush"
age = 21
cgpa = 8.5
is_student = True

print(name)
print(age)

# Variables should be descriptive

# Bad:

# x = 95

# Better:

student_score = 95

# ------------------------------------------

# EXPRESSIONS

# ------------------------------------------

# Expressions produce values

print(2 + 2)
print(2 > 1)
print(2 > 5)

# ------------------------------------------

# STRINGS

# ------------------------------------------

course = "Python for Machine Learning"

# Indexing

print(course[0])

# Slicing

print(course[0:6])

# Negative indexing

print(course[-1])

# String methods

print(course.upper())
print(course.lower())
print(course.title())

# Find

print(course.find("Machine"))

# Replace

print(course.replace("Python", "Learn"))

# Membership operator

print("Python" in course)

# ------------------------------------------

# ESCAPE SEQUENCES

# ------------------------------------------

print("Hello\nWorld")
print("This is a \\ backslash")

# ------------------------------------------

# STRING FORMATTING

# ------------------------------------------

first = "Tarush"
last = "Kumar"

full_name = f"{first} {last}"

print(full_name)

# ------------------------------------------

# NUMBERS & OPERATORS

# ------------------------------------------

a = 10
b = 3

# Arithmetic

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor Division
print(a % b)   # Modulus
print(a ** b)  # Exponent

# ------------------------------------------

# COMPARISON OPERATORS

# ------------------------------------------

# == Equal To

print(10 == 10)

# != Not Equal To

print(10 != 5)

# >

print(10 > 3)

# <

print(10 < 3)

# >=

print(10 >= 10)

# <=

print(10 <= 10)

# ------------------------------------------

# TYPE CONVERSION

# ------------------------------------------

x = "10"

print(int(x))
print(float(x))
print(bool(x))
print(type(x))

# ------------------------------------------

# CONDITIONAL STATEMENTS

# ------------------------------------------

temperature = 32

if temperature > 30:
    print("Hot Day")

elif temperature > 20:
    print("Good Day")

else:
    print("Cold Day")

# ------------------------------------------

# LOGICAL OPERATORS

# ------------------------------------------

age = 20
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)

# ------------------------------------------

# SHORT CIRCUIT ANALYSIS

# ------------------------------------------

x = 0

# Second condition never executes

print(x != 0 and (10 / x))

# OR stops early

print(True or False)


# -------------------------------------------

# For..else

# -------------------------------------------

successful = False
for _ in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# in the above example try running it with successful = True and observe the difference
# else block executes only when the loop does not exit early

print("\nWeek 1 Day 1 Complete")
