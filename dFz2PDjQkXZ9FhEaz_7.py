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

letter_check=lambda l:not set(l[1].lower())-set(l[0].lower())

