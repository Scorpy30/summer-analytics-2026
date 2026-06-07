# Week 1 - Day 1 Notes

# Python + Developer Workflow + Intro to ML

---

# 1. Why Everyone Needs Python

Python is used across many domains:

* Data Analysis
* Data Science
* AI / Machine Learning
* Automation
* Web Applications
* Mobile Apps
* Desktop Applications
* Testing
* Cybersecurity

Examples of companies using Python:

* Google
* Spotify
* Dropbox

---

## Why Python became popular

### Reason 1 — Solve complex problems quickly

Python allows solving problems in fewer lines of code.

Example → Extract first 3 characters

### C#

```csharp
str.Substring(0,3)
```

### JavaScript

```javascript
str.substring(0,3)
```

### Python

```python
str[0:3]
```

Cleaner and shorter.

---

### Reason 2 — Multipurpose language

One language can be used across multiple industries.

---

### Reason 3 — High-Level Language

Closer to human language than machine language.

---

### Reason 4 — Cross Platform

Code works across:

* Windows
* Linux
* macOS

---

### Reason 5 — Huge Community

Large developer support.

---

### Reason 6 — Large Ecosystem

Thousands of libraries available.

---

## Python Versions

Python 2

* Officially discontinued
* Support ended around 2020

Current:

```text
Python 3
```

---

# 2. PATH Variable

Question discussed:

> Why do we add Python to PATH?

PATH allows running programs directly from terminal.

Without PATH:

```text
C:\Python\python.exe
```

With PATH:

```text
python
```

Terminal automatically locates executable.

---

# 3. Expressions

Definition:

An expression is a piece of code that produces a value.

Examples:

```python
2 + 2
```

Output:

```text
4
```

```python
2 > 1
```

Output:

```text
True
```

```python
2 > 5
```

Output:

```text
False
```

---

# 4. Python Execution Flow

Execution pipeline:

```text
.py file
↓

Python Interpreter

↓

Bytecode

↓

Python Virtual Machine (PVM)

↓

Output
```

---

## Interpreter

Software program that:

* Reads Python code
* Converts instructions
* Detects syntax issues
* Sends executable form forward

A Pyhton Interpreter performs a two stage translation:


### 1. Compilation to Bytecode

Intermediate representation -> low-level compact instruction set.
Interpreter checks your code for syntax error. If it looks good, it translates the text into bytecode which is stored in `.pyc` files within a 
`__pycache__` folder.

Properties:

* Platform independent
* Faster than repeatedly parsing source


### 2. Python Virtual Machine (PVM)

Acts like software CPU readiing bytecode instructions and excecuting them line by line on your actual hardware.

Responsibilities:

* Reads bytecode
* Executes instructions

---

## Execution Modes

### Interactive Mode (REPL)

REPL:

```text
Read
Evaluate
Print
Loop
```

Used for:

* Quick testing
* Experimentation

---

### Script Mode

Code inside:

```text
program.py
```

Used for:

* Real projects
* Reusable code

---

# 5. PEP & Linting

## PEP

Python Enhancement Proposal

Purpose:

* Standard formatting
* Styling conventions
* Consistent code

Example:

Bad:

```python
x=1
```

Good:

```python
x = 1
```

---

## Linting

Linting checks:

* Syntax errors
* Bad formatting
* Potential bugs
* Style violations

Examples:

* Variable naming issues
* Missing spaces
* Unused imports

VS Code often auto-highlights these.

---

# 6. Useful VS Code Productivity

## Duplicate current line

```text
Shift + Alt + Down
Shift + Alt + Up
```

Use:

* Copy same line quickly

---

## Move line

```text
Alt + ↑
Alt + ↓
```

Use:

* Reorder code

---

## Multi Cursor

```text
Alt + Click
```

Use:

* Edit multiple places

---

## Comment code

```text
Ctrl + /
```

---

## Open terminal

```text
Ctrl + `
```

---

## Command Palette

```text
Ctrl + Shift + P
```

---

## To View Potential Problems(Linting)

```text
Ctrl + Shift + M
```
One another method is to go to setting and perform this task on save.

---

# 7. Python Implementations

Default:

## CPython

Written in:

```text
C
```

Produces:

```text
Bytecode
```

---

Other implementations:

### Jython

Runs on:

```text
JVM
```

Allows Java interoperability.

---

### IronPython

Runs on:

```text
.NET CLR
```

---

Why multiple implementations?

Different goals:

* Performance
* Integration
* Platform support

---

# 8. Variables

Rules:

Good:

```python
student_score
```

Bad:

```python
x
```

Guidelines:

* Meaningful
* Descriptive
* snake_case

---

# 9. Strings

Create:

```python
name = "Tarush"
```

Multiline:

```python
"""
Hello
This is an example
OF MULTIPLE LINES AND FORMATTED TEXT IN
P Y T H O N
"""
```

---

## String Slicing

```python
msg = "apple"
```

### 1.
```python
msg[0:3]
```

Returns: First three characters of string
```text
app
```

### 2.
Negative indexing:

```python
msg[-1]
```
Returns: Last character
```text
e
```

### 3.
```python
msg[0:]
```
Returns: Full String
```text
apple
```

### 4.
```python
msg[:3]
```
Returns: First 3 characters. Python automatically sets start index to `0`
```text
app
```

### 5.
```python
msg[:]
```
Returns: Copy of the original string.
```text
apple
```

### 5.
```python
msg[1:-1]
```
Returns: From character at index 1 to second last character. (Excludes `-1` i.e. the last charcter; as is the rule of slicing)
```text
ppl
```

---

# Escape Sequences

```python
\'
\"
```
USE > Single quote or Double quotes

```python
\\
```
USE > Backslash

```python
\n
```
USE > New line

---

# String Formatting

```python
first="John"
last="Doe"

f"{first} {last}"
```

---

# String Methods

Upper:

```python
course.upper()
```

Title:

```python
course.title()
```
Use:
```text
Converts First Letter Of Each Word To Caps
```

Strip spaces:

```python
course.strip()
```

Replace:

```python
course.replace("a","b")
```

Find:

```python
course.find("python")
```

Membership:

```python
"py" in course
```

Returns Boolean.

---

# 10. Numbers

Types:

```text
int
float
complex
```

Example:

```python
1 + 2j
```

---

# Arithmetic Operators

## Addition

```python
+
```

Adds values.

---

## Subtraction

```python
-
```

Subtracts values.

---

## Multiplication

```python
*
```

Multiply.

---

## Division

```python
/
```

Returns decimal result.

---

## Floor Division

```python
//
```

Returns integer quotient.

Example:

```python
10 // 3
```

Output:

```text
3
```

---

## Modulus

```python
%
```

Returns remainder.

Example:

```python
10 % 3
```

Output:

```text
1
```

---

## Exponent

```python
**
```

Power operation.

Example:

```python
10 ** 3
```

Output:

```text
1000
```

---

# Useful Functions

```python
abs()
```

Absolute value.

```python
round()
```

Round number.

Math module:

```python
import math
```

Functions:

```python
math.ceil()
math.floor()
math.fabs()
math.copysign()
```

---

# Type Conversion

```python
int()
float()
str()
bool()
type()
```

---

# Boolean Values

Falsy:

```text
0
""
[]
{}
None
```

Everything else → Truthy.

---

# 11. Comparison Operators

## Equal To

```python
==
```

Checks whether two values are equal.

---

## Not Equal To

```python
!=
```

Checks whether values differ.

---

## Greater Than

```python
>
```

---

## Less Than

```python
<
```

---

## Greater Than Equal

```python
>=
```

---

## Less Than Equal

```python
<=
```

Returns:

```text
True / False
```

---

## Chaining comparison operators
```text
Let a case be where age must be between 18 and 65
```

General Method:
```python
if age >= 18 and age < 65:
    print("Eligible")
```

Chaining Method:
```python
if 18 <= age > 65:
    print("Eligible")
```

---

## Ternary operators

Helpful in writing cleaner codes. For example:
Instead of -

```python
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
```

We can use -
```python
message = "Eligible" if age >= 18 else "Not eligible"
```

This is much cleaner.

---

# 12. Conditional Statements

Syntax:

```python
if condition:
    pass

elif condition:
    pass

else:
    pass
```

---

# 12.1 Logical Operators:

## and

All conditions must be True.

## or

Any condition must be True.

## not

Reverses Boolean value.

---

# 12.2 Short Circuit Analysis

## What is Short Circuit Evaluation?

Python evaluates logical expressions only until the final result becomes known.

If Python can determine the answer early, it skips evaluating remaining conditions.

Purpose:

* Faster execution
* Avoid unnecessary computation
* Prevent runtime errors

---

## Short Circuit with `and`

Rule:

For `A and B`

If `A` is False → Python stops immediately.

Example:

```python
age = 16

age >= 18 and print("Eligible")
```

Evaluation:

```text
age >= 18 → False
```

Second condition never executes.

Reason:

```text
False AND anything = False
```

---

Example:

```python
x = 0

x != 0 and (10 / x)
```

Evaluation:

```text
x != 0 → False
```

Python skips:

```python
10 / x
```

Avoids:

```text
ZeroDivisionError
```

---

## Short Circuit with `or`

Rule:

For `A or B`

If `A` is True → Python stops immediately.

Example:

```python
username = "admin"

username == "admin" or check_permission()
```

Evaluation:

```text
username == "admin"
→ True
```

Python never runs:

```python
check_permission()
```

Reason:

```text
True OR anything = True
```

---

## Return Behaviour

Logical operators return actual values, not only `True` / `False`.

Examples:

```python
10 or 20
```

Output:

```text
10
```

Because first value is truthy.

---

```python
0 or 20
```

Output:

```text
20
```

Because first value is falsy.

---

```python
10 and 20
```

Output:

```text
20
```

Returns last evaluated value.

---

```python
0 and 20
```

Output:

```text
0
```

Stops immediately.

---

## Real Use Cases

### Default Values

```python
name = user_input or "Guest"
```

If input is empty:

```text
Guest
```

---

### Safe Access

```python
user and user.email
```

Avoids accessing email when user is None.

---

# 13. Loops

Example:

```python
for attempt in range(3):
```

Range examples:

```python
range(3)
range(4,10)
```

---

## break

Terminate loop early.

---

## else in loops

Runs if loop completed without break.

---

# 14. Introduction to Machine Learning

Definition:

Machine learns patterns from experience instead of explicit instructions.

Term introduced by:

```text
Arthur Samuel (1959)
```

---

ML Workflow:

```text
Collect Data
↓

Feature Engineering
↓

Train/Test Split

↓

Training

↓

Evaluation

↓

Improve
```

Notes:

* Features should represent actual problem signals
* Train data builds model
* Test data evaluates reliability

---

## Additional

My keybinding for the run button that comes with the python extension:

```text
Ctrl + R Ctrl + P
```


# End of Day 1
