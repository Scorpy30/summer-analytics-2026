# Day 2 Questions

## Python Memory

1. Why does every Python object store a reference count?

2. Why is reference counting needed when Python already has garbage collection?

3. How much memory does a Python integer actually occupy?

4. What happens internally when reference count reaches zero?

---

## Lists vs NumPy

5. Why do Python lists store references instead of raw values?

6. What trade-off does Python gain by storing objects this way?

7. How much memory can NumPy save compared to Python lists?

---

## NumPy Internals

8. Why are NumPy arrays stored contiguously?

9. How does contiguous memory improve performance?

10. What exactly is vectorization?

11. How does broadcasting work internally?

12. Why are NumPy operations implemented in C?

---

## Views & Copies

13. Why do NumPy slices return views by default?

14. When should `.copy()` be used?

15. How can we determine whether two arrays share memory?

---

## Practical Questions

16. When should Python lists be preferred over NumPy arrays?

17. When does NumPy stop being the best choice?

18. Why are nested loops often slower than vectorized operations?

---

## My Questions

19. What is the exact difference between an iterable and an iterator?

20. How does Python know where an object exists in memory?

21. Why does NumPy feel like a matrix language compared to Python lists?

22. Python's id() function to see exactly when two variables share the same memory layout.

23. NumPy's bulit in .base attribute?

24. How the .view() method creates a shallow copy that still shares data.

25. How to use the is keyword to instantly check if two variables point to the exact same object in memory.

Status:

🔍 To Explore
