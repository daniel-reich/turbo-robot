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
  lwrstnc = ''
  for i in sentence:
    lwrstnc += i.lower()
  lwrlst = lwrstnc.split()
  tracker = 1
  for j in lwrlst:
    sticker = 0
    ssticker = 0
    if 's' in j:
      sticker += 1
    for k in range(len(j)-1):
      if j[k] == 's' and j[k+1] == 's':
        ssticker += 1
    if sticker <= ssticker:
      tracker *= 1
    else:
      tracker *= 0
  return tracker == 1

