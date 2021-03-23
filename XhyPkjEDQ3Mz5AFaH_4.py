"""


Given an input string `s` and a pattern `p`, implement regular expression
matching with support for "." and "*" .

### Examples

    is_match("aa", "a") ➞ false
    # "a" does not match the entire string "aa".
    
    is_match("aa", "a*") ➞ true
    # "*" means zero or more of the preceding element, "a".
    # Therefore, by repeating "a" once, it becomes "aa".
    
    is_match("ab", ".*") ➞ true
    # ".*" means "zero or more (*) of any character (.)".

### Notes

  * `s` could be empty and contains only lowercase letters a-z.
  * `p` could be empty and contains only lowercase letters a-z, and characters like . or *.

"""

import re
def is_match(s, p):
  t=s*2
  p=r'{}'.format(p)
  if '*' not in p and '.' not in p:
    return re.match(s,t).group()==re.match(p,t).group()
  else:
    return bool(re.match(p,s))

