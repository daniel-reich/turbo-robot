"""


Create a function which adds spaces before every capital in a word.
Uncapitalize the whole string afterwards.

### Examples

    cap_space("helloWorld") ➞ "hello world"
    
    cap_space("iLoveMyTeapot") ➞ "i love my teapot"
    
    cap_space("stayIndoors") ➞ "stay indoors"

### Notes

The first letter will stay uncapitalized.

"""

import re
def cap_space(txt):
  return re.sub('[A-Z]', lambda x: ' '+x.group(0).lower(), txt)

