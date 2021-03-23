"""


 **The caret** `^`, when found at the start of a characer set, is the
equivalent to "not" in RegEx. The regular expression `[^a-c]` matches any
characters except "a", "b" and "c". Write the **regular expression** that
matches any characters except letters, digits and spaces. You must use a
negated character set in your expression.

### Examples

    txt = " alice15@gmail.com "
    pattern = "yourregularexpressionhere"
    
    re.findall(pattern, txt) ➞ ["@", "."]

### Notes

  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and negation in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = "[^a-zA-Z1-9  ]"

