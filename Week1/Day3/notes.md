# Week 1 - Day 3 Notes

# Pandas — Data Manipulation & Thinking in Tables

---

# 1. Introduction

Pandas is a Python library used for:

* storing tabular data
* cleaning data
* filtering data
* transforming data
* analyzing data

Import:

```python
import pandas as pd
```

---

# 2. DataFrame Mental Model

Think of DataFrame as:

```text
Columns
↓
Series
↓
Values
```

Example:

| name | age |
| ---- | --- |
| A    | 21  |
| B    | 22  |

Each column behaves like a Series.

---

# 3. Selecting Data

Single column:

```python
bios["name"]
```

Result:

```text
Series
```

---

Multiple columns:

```python
bios[[
"name",
"age"
]]
```

Result:

```text
DataFrame
```

Question:

Why different outputs?

Because selection rules differ.

---

# 4. Boolean Filtering

One of the most important ideas.

Example:

```python
mask = (
    bios["age"] > 25
)

bios[mask]
```

Mental model:

```text
condition
↓
True False True
↓
DataFrame receives mask
↓
keep matching rows
```

Equivalent thinking:

```text
row1 → keep
row2 → remove
row3 → keep
```

---

Multiple conditions:

```python
bios[
(
bios["age"] > 20
)
&
(
bios["score"] > 90
)
]
```

Important:

Use:

```python
&
|
```

not:

```python
and
or
```

for Series.

---

# 5. String Methods

Example:

```python
bios["name"].str.contains(
"John"
)
```

Output:

```text
True
False
True
```

Question:

What happens internally?

Pandas:

```text
take row
↓
check condition
↓
return boolean
```

---

Startswith:

```python
.str.startswith()
```

Endswith:

```python
.str.endswith()
```

---

# 6. Regex Thinking

Regex means:

Pattern Matching.

Example:

```python
.str.contains(
r"^[A-Z]"
)
```

Question:

Why warning appeared?

Because regex engine interpreted symbols.

Important:

Literal text ≠ regex pattern

---

Extract:

```python
.str.extract()
```

Purpose:

Capture values.

Contains:

```python
.str.contains()
```

Purpose:

Return True / False.

---

# 7. Missing Values

Check:

```python
df.isna()
```

Count:

```python
df.isna().sum()
```

Remove:

```python
df.dropna()
```

Fill:

```python
df.fillna()
```

Question:

Should we remove or fill?

Depends.

Removing:

Pros:

* simple

Cons:

* data loss

---

Filling:

Pros:

* preserve rows

Cons:

* assumptions introduced

---

# 8. Creating Columns

Method 1

```python
df["new"] =
df["old"] * 2
```

---

Method 2

```python
apply()
```

---

Method 3

```python
map()
```

---

Method 4

```python
np.where()
```

Question:

Which is best?

Prefer:

Vectorized solutions.

---

# 9. Sorting & Ranking

Sort:

```python
sort_values()
```

Ranking:

```python
rank()
```

Question:

When ties occur?

Ranking strategy matters.

---

# 10. Datetime

Convert:

```python
pd.to_datetime()
```

Common mistake:

Passing DataFrame instead of Series.

Good:

```python
df["date"]
```

not:

```python
df
```

---

# 11. Pandas Philosophy

Do not think:

```text
row
↓
loop
↓
edit
```

Think:

```text
column
↓
transform
↓
assign
```

---

# Doubt Clearance

---

# 1. Why does this work?

```python
bios[
    bios['born_country'].isin(
        ["USA", "FRA", "GBR"]
    )
    &
    (
        bios['name'].str.startswith(
            "Keith"
        )
    )
]
```

I understand inner returns True/False.

But why does outer `bios[...]` accept booleans?

Why not error like `bios[1]`?

---

Answer:

Because DataFrame brackets (`[]`) are overloaded.

They mean different things depending on input type.

Examples:

```python
bios["name"]
```

Input:

```text
string
```

Meaning:

```text
select column
```

---

```python
bios[mask]
```

Input:

```text
Boolean Series
```

Meaning:

```text
boolean filtering
```

---

```python
bios[0:5]
```

Input:

```text
slice
```

Meaning:

```text
row slicing
```

---

This:

```python
bios[1]
```

fails because integer is not valid.

Internally:

```text
mask

0 True
1 False
2 True

↓

DataFrame scans rows

↓

keep row 0
drop row 1
keep row 2
```

So outer `bios[...]` does not receive booleans.

It receives:

```text
Series(dtype=bool)
```

which pandas recognizes specially.

---

# 2. head vs head()

Question:

Why different?

Answer:

```python
bios.head
```

returns:

```text
method object
```

Meaning:

"You are pointing at the function."

Example:

```python
print(bios.head)
```

Output:

```text
<bound method>
```

---

```python
bios.head()
```

executes function.

Returns:

```text
first 5 rows
```

Think:

```text
head
↓

function

head()

↓

run function
```

---

# 3. Why does .drop() need inplace=True but creating columns doesn't?

Question:

```python
df.drop(...)
```

vs

```python
df["new"] = ...
```

---

Answer:

Different operations.

This:

```python
df.drop()
```

returns NEW dataframe.

```text
old df
↓

new df
```

Nothing changes unless:

```python
df = df.drop(...)
```

or

```python
inplace=True
```

---

But:

```python
df["new"] = ...
```

means:

```text
modify existing dataframe
```

Equivalent idea:

```python
dictionary["key"] = value
```

You are assigning.

Not returning.

---

# 4. Why is this wrong?

```python
bios_new['born_date'] =
pd.to_datetime(
    bios_new
)
```

Answer:

You passed:

```text
whole dataframe
```

Expected:

```text
Series
array
date values
```

Correct:

```python
bios_new['born_date'] =
pd.to_datetime(
    bios_new['born_date']
)
```

Mental model:

Wrong:

```text
Convert TABLE
↓
store inside COLUMN
```

Correct:

```text
Convert COLUMN
↓
store inside COLUMN
```

---

# 5. Explain this

```python
bios[
bios['name']
.str.contains(
r'(?i)apple'
)
]
```

Why no `re.search()`?

Answer:

Pandas already calls Python regex engine internally.

Conceptually:

```text
for row in column:

re.search()

↓

return True/False
```

Equivalent idea:

```python
apply(
lambda x:
bool(
re.search()
)
)
```

But optimized.

---

# 6. Why warning for:

```python
.str.contains(
r'(.)\1'
)
```

This answer earlier had one mistake.

The warning is NOT because pandas thinks extraction is definitely intended.

Actual reason:

Capture groups exist.

`.contains()` ignores captured values.

Pandas warns because users often accidentally use:

```python
contains()
```

when they meant:

```python
extract()
```

Nothing broke.

Your regex still worked.

---

# 7. Is regex=True removing warning?

Not exactly.

This earlier explanation was slightly inaccurate.

`regex=True` is already default.

It does NOT suppress capture-group warning.

Better:

If you only want matching:

```python
r'(?:.)\1'
```

No.

That breaks.

Because backreferences need capture groups.

So warning is informational.

Ignore it.

---

# 8. Why doesn't:

```python
r'(.)\1
```

match Aaron?

Answer:

Regex is case-sensitive.

Engine sees:

```text
A
a
```

Different characters.

Use:

```python
.str.lower()
```

or

```python
(?i)
```

Example:

```python
r'(?i)(.)\1'
```

---

# 9. Why fill Unknown instead of dropping?

Question:

If later I remove Unknown anyway,
why add it?

Answer:

Three reasons.

1.

Preserve rows.

2.

Prevent later crashes.

3.

Keep reports readable.

Example:

```text
NaN
```

vs

```text
Unknown
```

But:

If missingness itself matters,

keep NaN.

Do not blindly fill.

---

# 10. Exactly two vowels:

Why this works?

```python
^[^AEIOU]*[AEIOU][^AEIOU]*[AEIOU][^AEIOU]*$
```

Answer:

It forces:

```text
whole string

↓

exactly

↓

2 vowels
```

No third vowel allowed.

Alternative (cleaner):

```python
.str.count(
r'(?i)[aeiou]'
)==2
```

Prefer this.

---

# 11. Why accented vowels broke regex?

Because:

```text
á ≠ a
ó ≠ o
```

Computers compare Unicode.

Normalize first:

```python
.normalize()
```

then filter.

---

# 12. Rank + sort bug

Wrong:

```python
bios['name']
.sort_values(
['height_rank']
)
```

Because:

Series cannot sort by another column.

Correct:

```python
bios
.sort_values(
by='height_rank'
)
['name']
```

Sort rows first.

Extract later. 

---

# 13. Why does this work?

```python
bios['name'].str.contains(
'abc'
)
```

but this does not?

```python
bios['name'].contains(
'abc'
)
```

Answer:

Because:

```text
Series
↓
contains() ❌
```

`contains()` is not a Series method.

String operations are grouped under:

```python
.str
```

So:

```python
bios['name']
.str
.contains()
```

means:

```text
Series
↓
String accessor
↓
String method
```

Think:

```text
Column
↓

Apply string operation row-by-row
```

---

# 14. Why can we do:

```python
bios['height'] > 180
```

without loops?

Answer:

Operators are overloaded.

This:

```python
bios['height'] > 180
```

conceptually behaves like:

```python
for value in column:
    value > 180
```

but optimized.

Output:

```text
True
False
True
```

not a single boolean.

---

# 15. Why are parentheses required?

Question:

```python
(
df['a'] > 5
)
&
(
df['b'] < 10
)
```

Why not:

```python
df['a'] > 5 & df['b'] < 10
```

Answer:

Operator precedence.

Python evaluates:

```text
&
before
comparisons
```

Parentheses force order.

Without them:

```text
expression becomes ambiguous
```

---

# 16. Why does this fail?

```python
if bios['age'] > 20:
```

Answer:

Because:

```python
bios['age'] > 20
```

returns:

```text
Series
```

Example:

```text
True
False
True
```

But:

```python
if
```

expects ONE boolean.

Use:

```python
.any()
```

or

```python
.all()
```

Example:

```python
(
bios['age'] > 20
).any()
```

---

# 17. Why:

```python
len(df)
```

does not mean total cells?

Answer:

DataFrame length means:

```text
number of rows
```

Use:

```python
df.shape
```

for:

```text
(rows, columns)
```

Total cells:

```python
df.size
```

---

# 18. Why does this happen?

```python
df['new'] = df['old']
```

Then modifying:

```python
df['new']
```

sometimes changes expectations.

Answer:

Assignment copies references.

DataFrame operations may share underlying memory.

When unsure:

```python
.copy()
```

---

# 19. Why use:

```python
axis=0
axis=1
```

Answer:

Think:

```text
axis=0
↓

move vertically
↓

operate column-wise
```

Example:

```python
sum rows
```

---

```text
axis=1
↓

move horizontally
↓

operate row-wise
```

Example:

```python
sum columns
```

Memory trick:

```text
0 → down

1 → across
```

---

# 20. Why does:

```python
sort_values()
```

not permanently sort?

Answer:

Pandas prefers immutability.

Usually:

```python
new_df =
df.sort_values()
```

Original stays unchanged.

Unless:

```python
inplace=True
```

---

Revision Complete

Things intentionally preserved:

* internal reasoning
* warnings
* pandas interpretation questions
* regex confusion
* masking mental models
* mutation confusion

---

# End of Day 3

Completed:

✅ DataFrames
✅ Selection
✅ Boolean filtering
✅ Regex
✅ Missing values
✅ Transformations
✅ Ranking
✅ Datetime
✅ Internal questioning
