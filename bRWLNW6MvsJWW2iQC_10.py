"""


Write three **regular expressions:** one called "nothing" that will match only
an empty string, one called "anything" that will match any string empty or
not, and one called "something" that will match non-empty strings only.

### Example

    txt1 = ""
    txt2 = "This is not an empty string."
    
    nothing = "yourregularexpressionhere"
    anything = "yourregularexpressionhere"
    something = "yourregularexpressionhere"
    
    bool(re.match(nothing, txt1)) ➞ True
    bool(re.match(nothing, txt2)) ➞ False
    re.findall(nothing, txt1) ➞ [""]
    re.findall(nothing, txt2) ➞ []
    
    bool(re.match(anything, txt1)) ➞ True
    bool(re.match(anything, txt2)) ➞ True
    re.findall(anything, txt1) ➞ [""]
    re.findall(anything, txt2) ➞ ["This is not an empty string."]
    
    bool(re.match(something, txt1)) ➞ False
    bool(re.match(something, txt2)) ➞ True
    re.findall(something, txt1) ➞ []
    re.findall(something, txt2) ➞ ["This is not an empty string."]

### Notes

  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
nothing = "^(?![\s\S])"
anything = "^.*"
something = ".+"

