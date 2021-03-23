"""


Create a function that takes a boolean variable `flag` and returns it as a
string.

### Examples

    bool_to_string(True) ➞ "True"
    
    bool_to_string(False) ➞ "False"

### Notes

  * Don't forget to return the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def bool_to_string(flag):
  if flag==True:
    return 'True'
  elif flag == False:
    return 'False'
  else:
    return 'Must be a boolean flag!'

