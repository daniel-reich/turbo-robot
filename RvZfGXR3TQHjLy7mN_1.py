"""


Write the **regular expression** that matches all street addresses. All street
addresses begin with a number. Use the character class `\d` in your
expression.

### Example

    txt = "123 Redding Dr. 1560 Knoxville Ave. 3030 Norwalk Dr. 5 South St."
    pattern = "yourregularexpressionhere"
    
    (re.findall(pattern, txt)) ➞ ["123 Redding Dr.", "1560 Knoxville Ave.", "3030 Norwalk Dr.", "5 South St."]

### Notes

  * You don't need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and character classes in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = r'\d+ \w+ \w+.'

