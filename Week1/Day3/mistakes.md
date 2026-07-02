# Mistakes & Lessons Learned

## Mistake 1

Used:

```python
.value_count()
```

Issue:

Method name incorrect.

Solution:

```python
.value_counts()
```

Lesson:

Plural methods matter.

---

## Mistake 2

Expected:

```python
bios[1]
```

to work.

Issue:

DataFrame brackets are overloaded.

Lesson:

`bios[...]` accepts:

* column names
* boolean masks
* slices

not arbitrary integers.

---

## Mistake 3

Used:

```python
bios_new['born_date'] = pd.to_datetime(bios_new)
```

Issue:

Passed entire DataFrame.

Lesson:

Convert the Series.

```python
bios_new['born_date'] =
pd.to_datetime(
    bios_new['born_date']
)
```

---

## Mistake 4

Expected `.drop()` to mutate automatically.

Lesson:

Most pandas operations return new objects.

---

## Mistake 5

Used regex without thinking about data type.

Lesson:

String methods fail on datetime columns.

Check:

```python
df.dtypes
```

first.

---

## Mistake 6

Assumed warning means failure.

Lesson:

Warnings often indicate:

* ambiguity
* performance concern
* possible misuse

not broken code.

---

## Mistake 7

Sorted Series while expecting DataFrame sorting.

Lesson:

Rows and columns behave differently.
