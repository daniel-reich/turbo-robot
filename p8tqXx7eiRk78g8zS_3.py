"""


Create a **regular expression** to check whether the given string is a valid
floating numeric character or not.

### Examples

    pattern = "yourregularexpressionhere"
    
    bool(re.match(pattern, "12.12")) ➞ True
    bool(re.match(pattern, "12.")) ➞ False
    bool(re.match(pattern, ".1")) ➞ True
    bool(re.match(pattern, "-.1")) ➞ True
    bool(re.match(pattern, "+4.4")) ➞ True
    bool(re.match(pattern, "+4")) ➞ False
    bool(re.match(pattern, "+4.4av")) ➞ False

### Notes

  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = "^[+-]?\d*\.{1}\d+$"

