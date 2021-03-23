"""


A pair of strings form a **strange pair** if both of the following are true:

  * The 1st string's **first** letter = 2nd string's **last** letter.
  * The 1st string's **last** letter = 2nd string's **first** letter.

Create a function that returns `True` if a pair of strings constitutes a
**strange pair** , and `False` otherwise.

### Examples

    is_strange_pair("ratio", "orator") ➞ True
    # "ratio" ends with "o" and "orator" starts with "o".
    # "ratio" starts with "r" and "orator" ends with "r".
    
    is_strange_pair("sparkling", "groups") ➞ True
    
    is_strange_pair("bush", "hubris") ➞ False
    
    is_strange_pair("", "") ➞ True

### Notes

It should work on a pair of empty strings (they trivially share nothing).

"""

def is_strange_pair(a, b):
  if len(a)>0 and len(b)>0:
    return (a[0]==b[-1])and (a[-1]==b[0])
  elif a == b:
    return True
  return False

