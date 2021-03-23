"""


Create a function that accepts a string of space separated integers and
returns the highest and lowest integers (as a string).

### Examples

    high_low("1 2 3 4 5") ➞ "5 1"
    
    high_low("1 2 -3 4 5") ➞ "5 -3"
    
    high_low("1 9 3 4 -5") ➞ "9 -5"
    
    high_low("13") ➞ "13 13"

### Notes

  * All integers are valid, no need to validate them.
  * There will always be at least one integer in the input string.
  * Output string must be two integers separated by a single space, and highest number is first.

"""

def high_low(txt):
  newlst = list(map(lambda x: int(x), txt.split(' ')))
  str1 = str(max(newlst))
  str2 = str(min(newlst))
  finalstr = str1 + " " + str2
  return finalstr

