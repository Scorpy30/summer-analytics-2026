# Week 1 - Day 2 Notes

# Python Iteration, Memory & NumPy Foundations

---

# 1. Iterables

An iterable is any object that can be traversed one element at a time.

Examples:

```python
name = "Tarush"
numbers = [1, 2, 3]
```

Both are iterable.(i.e. Strings and Lists)

Python internally retrieves elements one by one during iteration.

---

## Iteration

Iteration means visiting each item sequentially.

Example 1: Lists are iterables

```python
for number in [1, 2, 3]:
    print(number)
```

Output:

```text
1
2
3
```

Example 2: Strings are iterables

```python
for x in "Python":
       print(x)
```

Output:

```text
P
y
t
h
o
n
```

## Custom iterables
We can also create custom objects which are iterables =>
e.g. 
```python
for item in shopping_cart:
       print(item)
```

---

# 2. The range() Function

Many beginners assume:

```python
range(1000000)
```

creates one million numbers.

Not true.

`range()` creates a lightweight range object; It too is an iterable.

Example:

```python
x = range(10)
print(x)
```

Output:

```python
range(0, 10)
```

Python generates values only when needed.

Benefits:

* Memory efficient
* Fast
* Ideal for loops

```python
print(type(range(5)))
```

Output:

```text
<class 'range'>
```
"Range is a complex data type"; We can iterate over it and thus used in a for loop.

---

# 3. While Loops

`For` iterates over iterables; `while` is used for iterating as long as a condition is true.

Example:

```python
number = 100
while number > 0:
       print(number)
       number //= 2
```

Here we are not iterating over an iterable object like in case of `for` loop but evaluating a task(condition).
Check out the [app.py](app.py) for some simple code snippets on working of while loop.

## Infinite loops

Loops that runs over until a break statement

```python
while True:
```
It is an infinite loop because it is always true.

```python
while True:
       command = input(">")
       print("ECHO", command)
       if command.lower() == "quit":
              break
```

---

# 4. Functions

Functions allow code reuse.

Example:

```python
def greet():
    print("Hello")
```

Call:

```python
greet()
```

---

## Arguments and Parameters

__Arguments__ are the values passed to a function whereas __Parameters__ are the place holders, the type and number of input defined for the functions.

Example:

```python
def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("How may I help you?")

greet("Tarush", "NLU")
greet("Rohit", "Sharma")
```

```text
Tarush NLU
Rohit Sharma
```

What can we infer:
1. The function code block is reused for both inputs.
2. `first_name` and `last_name` are the __Parameters__ of the function `greet()`
3. The actual values passed to the function (when we called it) are the __Arguments__

## Types of functions
1. Performs a task
2. Return a value

Example 1:

```python
def greet(name):
       print(f"Hi {name}")
```
The functions `greet()` and `print()` does not return a value just perform a task.

Example 2:
```python
def addition(a,b):
       return a + b

addition(2,3)
```
The function `addition()` returns a value [sum of two numbers]

---

## Keyword Arguments

Keyword arguments are arguments passed to a function by explicitly stating both the parameter name and its value (e.g., name="Alice"). This is different from positional arguments, where the order of the inputs determines which variable they belong to.

### How Keyword Arguments Work
When you use keyword arguments, the order of the inputs does not matter because you are explicitly naming each one.

```python
def greet(firstname, lastname):
    print(f"Hello, {firstname} {lastname}!")

# Positional arguments (Order matters)
greet("John", "Doe")  
# Output: Hello, John Doe!
greet("Doe", "John") 
# Output: Hello, Doe John!

# Keyword arguments (Order does NOT matter)
greet(lastname="Doe", firstname="John")  
# Output: Hello, John Doe!
```

### The Key Benefits
1. __Better Readability:__ Anyone reading your code immediately knows what each value means without looking up the function definition.

2. __Safer Default Values:__ Functions can have optional parameters with preset defaults. Keyword arguments let you skip to the specific optional parameter you want to change.

3. __Order Flexibility:__ You can pass arguments in whatever sequence makes the most sense to you.

---

### Mixing Positional and Keyword Arguments
You can mix both types in a single function call, but Python enforces one strict rule: __positional arguments must always come first__

```python
# This works perfectly:
greet("John", lastname="Doe")

# This causes a SyntaxError:
greet(firstname="John", "Doe")
```

---

### Default Parameters

Default parameters are values assigned to function arguments in the function definition. If the caller does not provide a value for that argument, Python automatically uses the default value.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Uses the default value for 'greeting'
greet("Alice")          # Output: Hello, Alice!

# Overrides the default value
greet("Bob", "Welcome") # Output: Welcome, Bob!
```

However remember the __golden rule__ : __Non-default arguments must always come first. 
Check out [app.py](app.py) for example.

---

### *args and **kwargs

- __*args__ (Positional): Captures extra arguments as a tuple. You use this when you don't know how many items a user will pass in by position.
- __**kwargs__ (Keyword): Captures extra arguments as a dictionary. You use this when you don't know how many named keyword arguments a user will pass in.

```python
def demonstrate_both(*args, **kwargs):
    print("args:", args)      # A tuple of positional inputs
    print("kwargs:", kwargs)  # A dictionary of named inputs

# Calling the function with both types
demonstrate_both(1, 2, 3, status="active", role="admin")

# Output:
# args: (1, 2, 3)
# kwargs: {'status': 'active', 'role': 'admin'}
```

---

# 5. Introduction to NumPy

__What is `NumPy`?__
NumPy (Numerical Python) is the foundational library for scientific computing and data analysis in Python. It provides high-performance, multi-dimensional array objects (called `ndarray`), mathematical functions to operate on these arrays, and tools for linear algebra and random simulations.

## 5.1 Why do we need NumPy?

Before NumPy, numerical operations were often performed using Python lists.

Example:

```python
numbers = [1, 2, 3, 4]
```

Lists are flexible.

They can store:

```python
[1, "hello", True, 3.14]
```

But this flexibility comes at a cost.

---

## 5.2. The Hidden Cost of Python Lists

A Python list does NOT store raw integers directly.

Instead:

```text
List
 ↓
References (Memory Addresses)
 ↓
Actual Python Objects
```

Each integer object contains:

* Reference Count
* Type Information
* Actual Value

This creates memory overhead.

---

Example:

```python
numbers = [1, 2, 3]
```

Stored more like:

```text
List
 ↓
Address
 ↓
Integer Object
```

rather than:

```text
1 2 3
```

directly.

---

__THE LIST__

Take a simple example of

```python
list = [42]

[ Slot 0 ] ---> Points to memory address 0xABC... -> 8 bytes of pointer
                  |
                  v
       THE INT OBJECT (at 0xABC)
       +------------------------------------+

       | Reference Count (8 bytes)          | -> Tracks memory management
       | Type Pointer    (8 bytes) --------+ -> Points to the "Int Class" definition

       | Value Payload   (8 bytes) [ 42 ]   | -> The actual number 42
       +------------------------------------+
```


__Counting the Bytes:__
When we say a standard C-style integer takes 4 to 8 bytes, we mean the computer only stores the raw value 42.In Python, that single number 42 inside a list costs:
- `8 bytes` inside the list to store the address `0xABC`.
- `24 bytes` for the object box sitting at `0xABC` (`8 bytes ref count` + `8 bytes type pointer` + `8 bytes for the number 42`).
__Total cost: `32 bytes`__ to store one single integer.

---

## 5.3 Why NumPy is faster

But when you use a NumPy array, Python strips away the entire `"Int Object"` box and the list pointers. It just dumps the raw 42 directly into a tight, sequential block of memory, exactly like C.

Thus, NumPy is faster; almost `50` time faster than native lists.

---

# 6. What Is a Reference?

A reference is simply an address pointing to an object.
Every time you assign an object to a variable or put it in a list, you create a reference to it.Python uses these arrows to automatically manage your computer's memory through a system called __Reference Counting__.

Example:

```python
a = 42
b = a
```

Now both variables point to the same object.

```text
a ─┐
   ├──► 42
b ─┘
```

---

## Reference Count

The 8-byte reference count is a hidden counter built into every single Python object.
It tracks exactly how many variables, lists, or dictionaries are currently looking at that specific object.

#### Why does it exist?
Python needs to know when it is safe to delete an object from your computer's RAM.


#### How does it work?
If the counter drops to zero, it means nothing in your code is using that object anymore. Python instantly deletes it to free up memory.

Python tracks:

```text
How many references point to an object?
```

Example:

```python
a = 42
```

Reference count = 1

```python
b = a
```

Reference count = 2

Python uses this information for memory management.

When count becomes zero:

```text
Object can be removed from memory.
```

#### An Everyday Example
- Imagine a dog running around a park. 
- The dog is the Object in memory. 
- The dog's leash is a Reference.
- If Mom holds a leash, the reference count is `1`.
- If Dad attaches a second leash, the reference count becomes `2`.
- If Mom lets go, the count drops to `1`.
- If Dad lets go, the count drops to `0`. 
- Since no one is holding the dog, it runs away (Python deletes it from memory).

---

## 7. Why NumPy Is Faster

1. NumPy removes most Python object overhead.
2. Fixed Type
3. Contiguous memory blocks

Instead of:

```text
List
 ↓
References
 ↓
Objects
```

NumPy stores:

```text
Raw Values
Raw Values
Raw Values
Raw Values
```

contiguously in memory.

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
```

Memory:

```text
1 2 3 4
```

stored together.

Benefits:

* Less memory
* Better cache efficiency
* Faster computation
* Vectorized operations

---

## 8. Python Lists vs. NumPy Arrays: Memory Allocation

The fundamental difference between a Python list and a NumPy array is **how they are stored in your computer's memory (RAM)**. This structure directly impacts their processing speed.

---

### 8.1. Python List (Random, Fragmented Memory)
A Python list does not actually store your data together. Instead, it stores **pointers (memory addresses)** that point to the actual objects scattered randomly across your system memory. 

*   **Characteristics:** Fragmented, overhead-heavy, slower to access because the computer must hop between addresses.

#### Visual Diagram: Python List
*Each `[ ]` is a block of RAM. Shaded blocks `[▓▓]` hold the actual data, while `[-->]` blocks hold the memory pointers.*

```text
       List Object (Contiguous array of pointers)
      ┌───────────┬───────────┬───────────┐
      │   Pointer │   Pointer │   Pointer │
      └─────┬─────┴─────┬─────┴─────┬─────┘
            │           │           │
            ▼           ▼           ▼
RAM:
  Address: 0x01      0x02      0x03      0x04      0x05      0x06
         ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
         │  [▓▓▓]  │  [   ]  │  [   ]  │  [▓▓▓]  │  [   ]  │  [▓▓▓]  │
         │ Element │  Empty  │  Empty  │ Element │  Empty  │ Element │
         │   #1    │         │         │   #3    │         │   #2    │
         └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
```

---

### 8.2. NumPy Array (Contiguous Memory)
A NumPy array stores the actual data values directly next to each other in one unbroken, consecutive block of memory. 

*   **Characteristics:** Packed tightly, zero overhead, highly efficient for your computer's CPU cache.

#### Visual Diagram: NumPy Array
*All data values are stored sequentially in a single, predictable memory block.*

```text
       NumPy Array (Single unbroken block)
      ┌─────────────────────────────────────────────────────────────┐
      │ Array Metadata (Data Type, Shape, Strides)                 │
      └─────────────────────────────┬───────────────────────────────┘
                                    │ points to start
                                    ▼
RAM:
  Address: 0x101     0x102     0x103     0x104     0x105     0x106
         ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
         │  [▓▓▓]  │  [▓▓▓]  │  [▓▓▓]  │  [   ]  │  [   ]  │  [   ]  │
         │ Element │ Element │ Element │  Empty  │  Empty  │  Empty  │
         │   #1    │   #2    │   #3    │         │         │         │
         └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
```

---

### Quick Comparison Summary

| Feature | Python List | NumPy Array |
| :--- | :--- | :--- |
| **Memory Allocation** | Scattered (Random references) | Contiguous (Next to each other) |
| **Data Types** | Mixed types allowed (Strings, Ints, Objects) | Homogeneous (All elements must be the same type) |
| **Cache Utilization** | Poor (Requires constant memory hopping) | Excellent (Loads whole blocks into CPU cache) |
| **Speed** | Slower | Up to 50x faster for numerical tasks |

---

# 9. Creating NumPy Arrays

Import:

```python
import numpy as np
```

---

From a list:

```python
arr = np.array([1, 2, 3])
```

---

2D Array:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

---

Common Constructors

```python
np.zeros((3, 3))
```

Creates:

```text
0 0 0
0 0 0
0 0 0
```

---

```python
np.ones((3, 3))
```

---

```python
np.full((3, 3), 5)
```

---

```python
np.random.rand(3, 3)
```

---

```python
np.eye(3)
```

Identity Matrix.

---

# 10. Dimensions, Shape and Size

Shape:

```python
arr.shape
```

Returns:

```text
(rows, columns)
```

Example:

```python
(3, 4)
```

---

Dimensions:

```python
arr.ndim
```

---

Total Elements:

```python
arr.size
```

---

# 11. Indexing & Slicing

Index:

```python
arr[0]
```

---

2D Access:

```python
arr[1, 2]
```

---

Slicing:

```python
arr[:, 1]
```

Entire second column.

---

```python
arr[1:3, 2:4]
```

Rows 1-2 and Columns 2-3.

---

# 12. Views vs Copies

Very important concept.

Example:

```python
arr = np.array([1, 2, 3, 4])

slice_arr = arr[0:2]
```

Many NumPy slices create views.

Meaning:

```text
Both point to same underlying memory.
```

Changing one may affect the other.

---

Safe Copy:

```python
copy_arr = arr.copy()
```

Now changes are independent.

---

# 13. Broadcasting

One of NumPy's most powerful features.

Example:

```python
arr = np.array([1, 2, 3])

arr + 5
```

Output:

```text
[6 7 8]
```

NumPy automatically expands the scalar.

No explicit loop required.

---

# 14. Matrix Pattern Problem

Example target:

```text
1 1 1 1 1
1 0 0 0 1
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1
```

One solution:

```python
output = np.ones((5, 5))

output[1:4, 1:4] = 0

output[2, 2] = 9
```

Important lesson:

Use slicing to target regions instead of writing nested loops.

---

# 15. Mental Model for NumPy

Think of NumPy arrays as:

```text
A tightly packed block of memory
```

rather than:

```text
A collection of independent Python objects
```

This single idea explains:

* Why NumPy is fast
* Why NumPy uses less memory
* Why vectorization works
* Why views exist
* Why broadcasting is possible

---

## 16. Important question that came to my mind

By definition of reference counter in python if:

```python
a = 10
b = a
b = b+2
print(a)
```

```text
shouldn't it give `12`?
```
#### `No`
`print(a)` will still output `10`.
This is a very common point of confusion! The reference counter tracks how many variables point to an object, but integers in Python are __immutable__ (they cannot be changed in place).

Here is exactly what happens step-by-step under the hood:

1. a = 10 -> Python creates an integer object `10` in memory. Variable `a` points to it. Reference count for 10: 1 (plus Python's internal references).

2. b = a -> Variable b is pointed to the exact same 10 object in memory. `Reference count for 10: 2`. At this exact moment, both a and b share the same memory address.

3. b = b + 2 -> Because integers are immutable, Python cannot modify the 10 object to become 12. Instead, Python calculates `10 + 2` and creates a brand new integer object `12` somewhere else in memory. Variable `b` is now pointed to this new `12` object.

4. Reference count changes: The reference count for `10` drops back down by `1` because `b` left. The reference count for the new `12` object becomes `1`.

5. print(a) -> Variable a never moved. It is still pointing to the original `10` object. Therefore, it prints `10`.


#### When would it change? 

__Mutable Objects__; My  logic would have been correct if I was using a mutable object, like a list, and modifying it in place:

```python
a = [10]
b = a        # Both point to the same list
b.append(2)  # Modifies the list in place without creating a new one

print(a)     # Output: [10, 2]
```

### Then I noticed a similar patter when using numpy

```python
a = np.array([1,2,3])
```

- When we use NumPy, the behavior depends entirely on how we modify the variable `b`. Because NumPy arrays are mutable (like Python lists), we can change their contents in place. 
- However, if we completely reassign the variable using the `=` operator, it creates a new object just like the integer example.
- Here are the two different scenarios:

       * Scenario 1: Modifying in place (Changes both `a` and `b`)
       If we use the `+=` operator, NumPy modifies the original array data directly in memory. Since `b` points to the exact same memory allocation as `a`, both variables will change.

       ```python
       import numpy as np
       a = np.array([1, 2, 3])
       b = a
       b += 2  # Modifies the data in place
       print(a)  # Output: [3 4 5]
       ```

       * Scenario 2: Reassigning the variable (Only changes `b`)
       If we use `b = b + 2`, Python evaluates the right side first `(b + 2)`, creates a brand new NumPy array in a different memory location to store those new values, and points `b` to it. Variable `a` is left pointing to the original array.

       ```python
       import numpy as np
       a = np.array([1, 2, 3])
       b = a
       b = b + 2  # Creates a NEW array object and reassigns 'b'
       print(a)  # Output: [1 2 3]
       print(b)  # Output: [3 4 5]
       ```

---

#### The Key Takeaway
* 
```python
b += 2
```
Mutates the existing object. Reference count stays the same. `a` changes.

* 
```python
b = b + 2
```
Creates a new object. Reference counts change. `a` stays the same.

It behaves differently depending on the data type: 
- `Integers/Strings/Tuples`: Both `+` and `+=` always create a __brand new object__ because they are immutable.

- `Lists/NumPy Arrays`: `+` creates a new object, but `+=` modifies the object in place because they are mutable.

---

In the programming world, this is known as __side effects__, and it is one of the most common sources of sneaky bugs in Python and data science.
To protect yourself from accidentally changing your original data in NumPy, you can explicitly create a clean copy using the `.copy()` method:

```python
import numpy as np

a = np.array([1, 2, 3])
b = a.copy()  # Clones the data into a brand new memory spot

b += 2        # Safe! This will NOT touch 'a'
print(a)      # Output: [1 2 3]
```

---

### Alternative solution of exercise 1 in [NumPy tutorial file](Week1_Day2_NumPy_tutorial.ipynb)

##### Alternative 1: Modifying a Single Matrix (Most Readable)
Instead of creating two separate arrays (output and z) and pasting one into the other, you can construct a single matrix of ones and target the inner sections directly via slicing.

```python 
import numpy as np

# Create the full 5x5 array of ones
output = np.ones((5, 5))

# Zero out the inner 3x3 section
output[1:4, 1:4] = 0

# Set the absolute center element to 9
output[2, 2] = 9

print(output)
```

##### Alternative 2:  Using np.pad (Functional Approach)
If you want to view this problem as building from the inside out, you can start with the single center value 9, pad it with a layer of zeros, and then pad that result with a layer of ones using `⁠np.pad`

```python
import numpy as np

# Start with the single center value as a 1x1 matrix
center = np.array([[9]])

# Pad with 1 layer of zeros around it to make it 3x3
inner = np.pad(center, pad_width=1, mode='constant', constant_values=0)

# Pad with 1 layer of ones around that to make it 5x5
output = np.pad(inner, pad_width=1, mode='constant', constant_values=1)

print(output)
```

###### Alternative 3: The One-Liner (Using np.zeros and Assignment)
You can instantiate a matrix of zeros, change the borders to ones, and place the 9 in the center.
```python
import numpy as np

# Initialize a 5x5 array with 0
output = np.zeros((5, 5))

# Set the outer frame to 1
output[[0, -1], :] = 1  # Top and bottom rows
output[:, [0, -1]] = 1  # Left and right columns

# Set the exact center to 9
output[2, 2] = 9

print(output)
```

##### Expected Output for All Solutions

All three alternatives will produce the exact matrix generated by your original script:

Output:

```text
[[1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 9. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]]
```

---

# End of Day 2

Completed:

- ✅ Iterables and iteration
- ✅ range() object
- ✅ Functions
- ✅ Python memory model
- ✅ References and reference counting
- ✅ NumPy arrays
- ✅ Shape and dimensions
- ✅ Indexing and slicing
- ✅ Views vs copies
- ✅ Broadcasting
- ✅ Matrix manipulation
