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
  for i in range(len(lst)):
    lst[i] = lst[i].lower()
  for item in lst[1]:
    if item not in lst[0]:
      return False
  return True

