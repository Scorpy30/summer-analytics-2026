# Day 3 Questions

## DataFrame Internals

1. Why does:

```python
bios[mask]
```

work?

Internal curiosity:

```text
DataFrame
↓
Receive Boolean Series
↓
Keep rows where value=True
```

How does pandas implement this?

---

2. Why does:

```python
bios["name"]
```

return a Series but:

```python
bios[["name"]]
```

return a DataFrame?

---

3. How does pandas know whether brackets mean:

* column selection
* filtering
* slicing

?

---

## Regex & String Operations

4. What did pandas think I meant when regex warnings appeared?

5. Why does:

```python
.str.contains()
```

return booleans while:

```python
.str.extract()
```

returns values?

6. When should regex be avoided?

7. Does regex scan entire columns row-by-row?

---

## Missing Values

8. Why does pandas use `NaN` instead of `None`?

9. What actually happens internally after:

```python
dropna()
```

10. Does:

```python
fillna()
```

create copies?

11. How much memory do missing values occupy?

---

## Data Transformation

12. Difference between:

```python
apply()
map()
replace()
where()
```

Internally:

* iteration?
* vectorization?
* broadcasting?

---

13. When should vectorized operations be preferred?

---

## Datetime

14. Why does:

```python
pd.to_datetime()
```

need Series instead of entire DataFrame?

15. How does pandas detect dates automatically?

---

## Performance

16. Why is pandas faster than loops?

17. When does pandas become slow?

18. Why do chained operations sometimes reduce readability?

---

## My Questions

19. What exactly does inplace do?

20. Why does pandas sometimes return views and sometimes copies?

21. How does pandas store mixed datatypes internally?

22. `bios[bios['name'].str.contains(r'[^AEIOUaeiou]', na = False)]` vs `bios[bios['name'].str.contains(r'^[^AEIOUaeiou]*$', na = False)]` from practice question 6

23. Insted of using :

    ```python
    import re
    # The manual, tedious way
    bios[bios['name'].apply(lambda x: bool(re.search(r'(?i)apple', str(x))))]
    ``` 

    ```python
    # Pandas automatically uses 're' for you here!
    bios[bios['name'].str.contains(r'(?i)apple', na=False)]
    ```
    Explain the working of above snippet.


24. sorry I forgot but somewhere in my notes it was written that inner bios[---] is returning boolean values True or False and outer bios is doing Boolean Filtering. It is displaying the rows with True and ignoreing the False.
so in this line - `bios[bios['born_country'].isin(["USA", "FRA", "GBR"]) & (bios['name'].str.startswith("Keith"))]` I am sure same thing is happening ... so why is outer bios taking in True or False values but inner one columns -> this is clear because the code I wrote does so but but, I don't have words but like how does or what actual values goes to a dataframe? like bios is a dataframe here if I try to write bios[1] : it is an error so why is bios[True] not an error like what values are going in what are coming out ... which data types and how each is processed.

25. head vs head()

26. why in .drop() we have to use inplace = True for actually changing dataframe but not while creating a new column?

27. bios_new['born_date'] = pd.to_datetime(bios_new) how is this wrong??

Status:

🔍 To Explore
