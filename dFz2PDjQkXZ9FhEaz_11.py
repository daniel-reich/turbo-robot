"""


Create a function that accepts a list of two strings and checks if the letters
in the second string are present in the first string.

### Examples

    letter_check(["trances", "nectar"]) ➞ True
    
    letter_check(["compadres", "DRAPES"]) ➞ True
    
    letter_check(["parses", "parsecs"]) ➞ False

### Notes

  * Function should not be case sensitive (as indicated in the second example).
  * Both strings are presented as a single argument in the form of a list.
  *  **Bonus:** Solve this without RegEx.

"""

def letter_check(lst):
  lst[0] = lst[0].lower()
  lst[1] = lst[1].lower()
  lst1 = list(lst[0])
  lst2 = list(lst[1])
  for i in lst2:
    if i not in lst1:
      return False
  return True

