# Day 1 Questions

## Python & Execution

1. Why does Python use an Interpreter → Bytecode → PVM pipeline instead of directly executing source code?

2. What exactly is bytecode and where is it stored?

3. How does the Python Virtual Machine actually execute instructions?

4. Why does Python have multiple implementations (CPython, Jython, IronPython, PyPy)?

5. If Python is interpreted, why does it still generate bytecode?

---

## Environment & Tooling

6. Why do we add some software to PATH but not others?

Notes:

* Which applications actually need PATH?
* Why can some applications run without PATH?
* What happens internally when terminal searches commands?

---

7. What is a sandbox?

Notes:

* Difference between sandbox and normal environment
* Why notebooks and cloud environments use sandboxes
* Security and isolation concepts

---

## REPL & Development Workflow

8. What is the actual point of using REPL inside VS Code?

Notes:

* When should REPL be preferred over script execution?
* Why not simply run `python` inside terminal?

---

9. How is REPL different from starting a terminal session and writing:

```bash id="l6g9pu"
python
```

Questions:

* Are they the same thing?
* Does VS Code add additional capabilities?
* How does state persist?

---

10. When should code move from REPL experimentation into `.py` files?

---

## Code Quality

11. What does linting actually analyze internally?

Questions:

* Syntax?
* Style?
* Performance?
* Bugs?

---

12. What is the difference between formatting and linting?

---

13. Why does PEP exist and who decides Python standards?

---

## Python Language

14. Why are strings immutable?

15. Why does slicing exclude the ending index?

16. Why does Python use indentation instead of braces?

17. Why do logical operators return values instead of only `True` / `False`?

18. How does short-circuit evaluation improve performance?

---

## Machine Learning

19. Why is feature engineering considered important?

20. How much data is usually enough to train a useful model?

21. Why do we split data into training and testing datasets?

---

# Bonus Questions for Later

* How does memory management work in Python?
* What happens internally when we import a module?
* Why is Python slower than C/C++?
* What makes notebooks useful for data science?

Status:

🔍 To Explore
