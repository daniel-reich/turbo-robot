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
  srt1 = sorted(lst[0].lower())
  srt2 = sorted(lst[1].lower())
  print(srt1)
  print(srt2)
  for chr in srt1:
    if chr not in srt2:
      srt1.remove(chr)
  return srt1 == srt2

