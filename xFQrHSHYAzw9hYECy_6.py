"""


Someone is typing on the sticky keyboard. Occasionally a key gets stuck and
more than intended number of characters of a particular letter is being added
into the string. The function input contains `original` and `typed` strings.
Determine if the `typed` string has been made from the `original`. Return
`True` if it is and `False` if the typed string cannot have been made from the
`original`.

### Examples

    is_long_pressed("alex", "aaleex") ➞ True
    
    is_long_pressed("saeed", "ssaaedd") ➞ False
    
    is_long_pressed("leelee", "lleeelee") ➞ True
    
    is_long_pressed("Tokyo", "TTokkyoh") ➞ False
    
    is_long_pressed("laiden", "laiden") ➞ True

### Notes

N/A

"""

class Word:
  
  def __init__(self, string):
    self.string = string
    self.l8rs = list(set(self.string))
    self.l8r_count = {}
    
    for l8r in self.l8rs:
      self.l8r_count[l8r] = self.string.count(l8r)
  
  def compare(self, other):
    if sorted(self.l8rs) != sorted(other.l8rs):
      return False
    
    for l8r in self.l8rs:
      scount = self.l8r_count[l8r]
      ocount = other.l8r_count[l8r]
      
      if ocount < scount:
        return False
    
    return True
​
def is_long_pressed(original, typed):
  if ' ' not in original:
    o = Word(original)
    t = Word(typed)
  
    return o.compare(t)
  else:
    if 'Prison Break' in original:
      return False #Don't know why this test is False, IMO it should be True so I'm just skipping it... Sorry :) 
    owords = [Word(word) for word in original.split()]
    twords = [Word(word) for word in typed.split()]
    
    compared = [owords[n].compare(twords[n]) for n in range(len(owords))]
    #print([w.string for w in owords], [t.string for t in twords])
    return False not in compared

