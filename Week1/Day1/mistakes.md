# Mistakes & Lessons Learned

## Mistake 1

Assumed Python executes `.py` files directly.

Issue:

Python first converts source code into bytecode before execution.

Lesson:

Execution flow:

```text
.py → Interpreter → Bytecode → PVM → Output
```

---

## Mistake 2

Ignored linting warnings.

Issue:

Linting warnings highlight formatting issues and possible mistakes.

Solution:

Read and fix warnings instead of disabling them.

---

## Mistake 3

Used unclear variable names.

Bad:

```python
x = 95
```

Better:

```python
student_score = 95
```

Lesson:

Code should be readable.

---

## Mistake 4

Expected all logical conditions to execute.

Issue:

Python uses short-circuit evaluation.

Lesson:

```text
and → stops at first False
or → stops at first True
```

---

## Mistake 5

Used terminal and REPL interchangeably.

Lesson:

REPL is useful for quick experiments.
Scripts are better for reusable programs.
