"""


A **Character Set** will match any characters within a pair of brackets `[ ]`.
You can specify a **range** of characters by using a **hyphen**.

    [abcd] == [a-d]

If the hyphen appears as the **first** or **last** character then it is
considered a **literal** hyphen.

    txt = "non-profit"
    pattern = "[abc-]"
    
    re.findall(pattern, txt) ➞ ["-"]

You can also use **character classes** in a character set.

    [a-zA-Z0-9_] == [\w]

Write the **regular expression** that will match an "x" followed by two
hexadecimal digits. A hexadecimal digit can be either one of the 10 decimal
digits (0 to 9) or a letter from A to F.

### Examples

    txt1 = "Exception 0xAF"
    txt2 = "Exception 0xD3"
    txt3 = "Exception 0xd3"
    txt4 = "Exception 0xZZ"
    pattern = "yourregularexpressionhere"
    
    re.findall(pattern, txt1) ➞ ["xAF"]
    re.findall(pattern, txt2) ➞ ["xD3"]
    re.findall(pattern, txt3) ➞ []
    re.findall(pattern, txt4) ➞ []

### Notes

  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and character sets in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
pattern = "x[A-F0-9]{2}"

