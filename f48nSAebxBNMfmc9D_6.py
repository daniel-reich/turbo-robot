"""


Write a function that receives a list of words and a mask. Return a list of
words, sorted alphabetically, that match the given mask.

### Examples

    scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “*re**”) ➞ [“creed”]
    
    scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “***”) ➞ [“dee”, “ree”]

### Notes

The length of a mask will never exceed the length of the longest word in the
word list.

"""

class Mask:
  
  def __init__(self, mask):
    self.mask = mask
  
  def match(self, possability):
    
    if len(self.mask) != len(possability):
      return False
    
    for n in range(len(self.mask)):
      if self.mask[n] == '*':
        continue
      else:
        if self.mask[n] != possability[n]:
          return False
    
    return True
​
def scrambled(words, mask):
  
  mask = Mask(mask)
  
  return list(sorted([word for word in words if mask.match(word) == True]))

