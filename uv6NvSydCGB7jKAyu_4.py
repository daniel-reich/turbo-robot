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

def is_parsel_tongue(sentence):
  words = sentence.lower().split(" ")
  for i in range(len(words)):
    if "s" in words[i]:
      if not("ss" in words[i]):
        return False
  return True

