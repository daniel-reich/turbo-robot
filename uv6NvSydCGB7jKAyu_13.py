"""


Hermione has come up with a precise formula for determining whether or not a
phrase was ssspoken by a parssseltongue ( _a reference from the Harry Potter
universe; the language of ssserpents and those who can converse with them_ ).

Each word in a sssentence must contain either:

  1. Two or more consecutive instances of the letter "s" (i.e. must be together `ss..`), or...
  2. Zero instances of the letter "s" by itself.

### Examples

    is_parsel_tongue("Sshe ssselects to eat that apple. ") ➞ True
    
    is_parsel_tongue("She ssselects to eat that apple. ") ➞ False
    # "She" only contains one "s".
    
    is_parsel_tongue("Beatrice samples lemonade") ➞ False
    # While "samples" has 2 instances of "s", they are not together.
    
    is_parsel_tongue("You ssseldom sssspeak sso boldly, ssso messmerizingly.") ➞ True

### Notes

N/A

"""

def is_parsel_tongue(s):
  lst = s.split(" ")
  for x in lst:
    count = 0
    for y in range(len(x)):
      if x[y] == 's' or x[y] == 'S':
        count += 1
      else:
        if count == 1:
          return False
        count = 0
  return True

