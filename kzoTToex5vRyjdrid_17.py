"""


Write the **regular expression** that will match all non-digit characters of a
string. Use the character class `\D` in your expression.

### Example

    txt = "242Edabit2345can3443be3254324addictive!"
    pattern = "yourregularexpressionhere"
    
    " ".join(re.findall(pattern, txt)) ➞ "Edabit can be addictive!"

### Notes

  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and character classes in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = "\D+"

