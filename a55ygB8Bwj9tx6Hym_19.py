"""


Return the smallest number of steps it takes to convert a string **entirely**
into uppercase or **entirely** into lower case, whichever takes the fewest
number of steps. A step consists of changing one character from lower to upper
case, or vice versa.

### Examples

    steps_to_convert("abC") ➞ 1
    # "abC" converted to "abc" in 1 step
    
    steps_to_convert("abCBA") ➞ 2
    # "abCBA" converted to "ABCBA" in 2 steps
    
    steps_to_convert("aba") ➞ 0
    
    steps_to_convert("abaCCC") ➞ 3

### Notes

  * Return `0` if empty string.
  * Return `0` if the string is already entirely in one case.
  * Only alphabetic characters.
  * Input has no spaces.

"""

def steps_to_convert(txt):
  count_upper = 0
  count_lower = 0
  if txt == '':
    return 0
  else:
    for x in txt:
      if x.islower():
        count_lower += 1
      elif x.isupper():
        count_upper += 1
    if count_lower >= count_upper:
      return count_upper
    elif count_upper > count_lower:
      return count_lower

