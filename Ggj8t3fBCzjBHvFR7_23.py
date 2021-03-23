"""


Write a **regular expression** that will match all the **positive** numbers in
a string with numbers separated by spaces. You must use RegEx **negative
lookbehind**.

    txt = "23 -43 34 -44 45 -55 56"
    pattern = "yourregularexpressionhere"
    
    re.findall(pattern, txt) ➞ ["23", "34", "45", "56"]

### Notes

  * You don't need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and negative lookbehind in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = "(?<![-\d+])\d+"

