# Day 3 Takeaways

* Learned that DataFrame filtering works through boolean masks.
* Understood how `.str.contains()` creates True/False outputs.
* Learned how regex integrates directly inside pandas string methods.
* Understood why `.extract()` and `.contains()` serve different goals.
* Learned multiple approaches to creating columns.
* Practiced handling missing values using `.dropna()` and `.fillna()`.
* Learned that pandas methods frequently return new objects.
* Understood ranking and sorting workflows.
* Practiced joins and aggregation operations.
* Learned that debugging warnings improves understanding.
* Built intuition for dataframe transformations.
* Learned to ask what pandas interprets internally instead of only reading syntax.
* Learnt use of `?i`
* Whenever you call `.str.contains()`, pandas takes the string pattern you typed and passes it directly into Python's internal `re` engine behind the scenes.
   If not then
   ```python
   import re
   # Standard match (fails because of case mismatch)
   print(re.search("apple", "Apple Pie"))  # Returns None
   
   # Inline flag match (succeeds)
   print(re.search("(?i)apple", "Apple Pie"))  # Returns a Match object
   ```
