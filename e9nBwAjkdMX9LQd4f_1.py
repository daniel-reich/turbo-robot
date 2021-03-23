"""


 **Fixed quantifiers** indicate numbers of characters or expressions to match.

`x{n}` matches **exactly** "n" occurrences of the preceding item "x":

    re.findall("a{2}", "candy") ➞ []
    re.findall("a{2}", "caandy") ➞ ["aa"]

`x{n,}` matches **at least** "n" occurrences of the preceding item "x":

    re.findall("a{2,}", "candy") ➞ []
    re.findall("a{2,}", "caandy") ➞ ["aa"]
    re.findall("a{2,}", "caaaaandy") ➞ ["aaaaa"]

`x{n,m}` matches **at least** "n" **and at most** "m" occurrences of the
preceding item "x":

    re.findall("a{1,3}", "cndy") ➞ []
    re.findall("a{1,3}", "candy") ➞ ["a"]
    re.findall("a{1,3}", "caandy") ➞ ["aa"]
    re.findall("a{1,3}", "caaaaandy") ➞ ["aaa"]

Write the **regular expression** to find the ellipsis (3 **or more** dots in a
row) in a string. You must use one of the 3 fixed quantifier above in your
expression.

### Example

    txt = "Hello!... Wait. How goes?..... GoodBye!.."
    pattern = "yourregularexpressionhere"
    re.findall(pattern, txt) ➞ ["...", "....."]

### Notes

  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and quantifiers in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
txt = 'Hello!... Wait. How goes?..... GoodBye!..'
pattern = '\.{3,}'
re.findall(pattern, txt)

