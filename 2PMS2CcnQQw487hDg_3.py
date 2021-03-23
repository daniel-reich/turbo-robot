"""


Write a **regular expression** that will match the states that voted **yes**
to President Trump's impeachment. You must use RegEx **positive lookahead**.

### Example

    txt = "Texas = no, California = yes, Florida = yes, Michigan = no"
    pattern = "yourregularexpressionhere"
    
    re.findall(pattern, txt) ➞ ["California", "Florida"]

### Notes

  * You don't need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * This is fake data and used only for educational purposes.
  * Find more info on RegEx and positive lookahead in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = "(\w+)(?= = yes)"

