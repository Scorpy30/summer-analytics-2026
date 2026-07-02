1. `bios[bios['name'].str.contains(r'[^AEIOUaeiou]', na = False)]` vs `bios[bios['name'].str.contains(r'^[^AEIOUaeiou]*$', na = False)]` from practice question 6

2. Insted of using :

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


3. sorry I forgot but somewhere in my notes it was written that inner bios[---] is returning boolean values True or False and outer bios is doing Boolean Filtering. It is displaying the rows with True and ignoreing the False.
so in this line - `bios[bios['born_country'].isin(["USA", "FRA", "GBR"]) & (bios['name'].str.startswith("Keith"))]` I am sure same thing is happening ... so why is outer bios taking in True or False values but inner one columns -> this is clear because the code I wrote does so but but, I don't have words but like how does or what actual values goes to a dataframe? like bios is a dataframe here if I try to write bios[1] : it is an error so why is bios[True] not an error like what values are going in what are coming out ... which data types and how each is processed.

4. head vs head()

5. why in .drop() we have to use inplace = True for actually changing dataframe but not while creating a new column?

6. bios_new['born_date'] = pd.to_datetime(bios_new) how is this wrong??

7. 