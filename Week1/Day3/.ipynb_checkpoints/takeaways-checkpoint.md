1. Whenever you call `.str.contains()`, pandas takes the string pattern you typed and passes it directly into Python's internal `re` engine behind the scenes.
   If not then
   ```python
   import re
   # Standard match (fails because of case mismatch)
   print(re.search("apple", "Apple Pie"))  # Returns None
   
   # Inline flag match (succeeds)
   print(re.search("(?i)apple", "Apple Pie"))  # Returns a Match object
   ```

2. Learnt use of `?i`

3. 

