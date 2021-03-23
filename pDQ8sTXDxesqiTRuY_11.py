"""


Write a **regular expression** that will help us count how many tall people
work in your company. You must use RegEx **positive lookbehind**.

### Example

    lst = ["tall height", "tall height", "short height", "medium height", "tall height"]
    pattern = "yourregularexpressionhere"
    
    len(re.findall(pattern, ", ".join(lst))) ➞ 3

### Notes

  * You don't need to write a function just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and positive lookbehind in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = "(?<=tall height)"

