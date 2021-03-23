"""


Regular Expressions (RegEx) are a powerful tool used to match or search for a
pattern in a string. To use them in Python you need to import the `re` module.
You can do this by adding the following line at the top of your file:

    import re

Write a **regular expression** that will match the files with the extension
`.py` or `.pyw`. You must use the RegEx **line anchor** `$`, which matches the
end of a string.

### Examples

    pattern = "yourregularexpressionhere"
    
    bool(re.search(pattern, "/users/file.py")) ➞ True
    bool(re.search(pattern, "/users/file.pyw")) ➞ True
    bool(re.search(pattern, "/users/python/file.txt")) ➞ False

### Notes

  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and line anchors in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = r'/[a-z]{5}/[a-z]{4}.[pyw]{2,3}$'
​
bool(re.search(pattern, '/users/file.py'))

