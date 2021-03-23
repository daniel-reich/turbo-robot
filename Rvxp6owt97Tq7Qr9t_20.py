"""


Regular Expressions (RegEx) are a powerful tool used to match or search for a
pattern in a string. To use them in Python you need to import the `re` module.
You can do this by adding the following line at the top of your file:

    import re

Write a **regular expression** that will match any file located within the
"users/edabit" directory. You must use at least one RegEx **line anchor**.

### Examples

    pattern = "yourregularexpressionhere"
    
    bool(re.search(pattern, "/users/edabit/python/regex.py")) ➞ True
    bool(re.search(pattern, "/users/edabitt/python/file.txt")) ➞ False
    bool(re.search(pattern, "/users/pyter/edabit/file.py")) ➞ False

### Notes

  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and line anchors in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = "^/users/edabit/"

