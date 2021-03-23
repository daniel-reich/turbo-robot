"""


By default **quantifiers** like `*` and `+` are "greedy", meaning that they
try to match as many characters as possible. Using `?` after the quantifier
makes the quantifier "lazy": meaning that it will stop as soon as it finds a
match.

    txt = "1232 2133424 809890 548"
    re.findall(".+\s", txt) ➞ ["1232 2133424 809890 "]
    re.findall(".+?\s", txt) ➞ ["1232 ", "2133424 ", "809890 "]

Write a **regular expression** to find all HTML comments in the text. You must
use lazy quantifiers in your expression.

    txt = "... <!-- My -- comment test --> ..  <!----> .. "
    pattern = "yourregularexpressionhere"
    
    re.findall(pattern, txt) ➞ ["<!-- My -- comment test -->", "<!---->"]

### Notes

  * HTML comments are formatted `<!--this is and HTML comment-->`.
  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and quantifiers in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = "<!.*?>"

