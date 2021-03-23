"""


Write a **regular expression** that ensures the word "end" is inside of
another word (e.g. "bending"). You must use RegEx **boundary assertions**.
Non-word characters such as `!`, `?`, etc. cannot be boundaries.

### Examples

    pattern = "yourregularexpressionhere"
    
    bool(re.search(pattern, "The end of the story.")) ➞ False
    bool(re.search(pattern, "Endings are pointless.")) ➞ False
    bool(re.search(pattern, "Let"s send!")) ➞ False
    bool(re.search(pattern, "We viewed the rendering at the end.")) ➞ True
    bool(re.search(pattern, "Sometimes bending the rules is good.")) ➞ True

### Notes

  * You cannot use `\w`, `*`, `.` or `+` in your expression.
  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and boundary assertions in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = r"\Bend\B"

