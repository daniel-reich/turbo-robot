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

def is_strange_pair(txt1, txt2):
​
  if len(txt1) > 0 and len(txt2) > 0:
    if(txt1[0] == txt2[-1] and txt2[0] == txt1[-1]):
      return True
  if len(txt1) == 0 and len(txt2) == 0:
    return True
  return False

