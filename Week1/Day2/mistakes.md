# Mistakes & Lessons Learned

## Mistake 1

Assumed:

```python
range(1000000)
```

creates one million numbers.

Lesson:

`range()` creates a lightweight range object and generates values when needed.

---

## Mistake 2

Treated Python lists as collections of raw values.

Lesson:

Lists store references to Python objects.

---

## Mistake 3

Assumed variables create new copies automatically.

Example:

```python
a = [1, 2, 3]
b = a
```

Lesson:

Both variables reference the same object.

---

## Mistake 4

Modified a NumPy slice expecting the original array to remain unchanged.

Lesson:

Many NumPy slices are views, not copies.

Use:

```python
arr.copy()
```

when independent data is required.

---

## Mistake 5

Used loops where slicing could solve the problem more cleanly.

Lesson:

NumPy operations should prefer vectorization and slicing.

---

## Mistake 6

Focused only on syntax instead of memory behavior.

Lesson:

Understanding memory layout explains most NumPy performance benefits.
