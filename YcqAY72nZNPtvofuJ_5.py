"""


Write a function that receives a list of _x_ integers and returns a list of
_x_ integers in the Nth term of a quadratic number sequence (where _x_ is the
length of the incoming list). Your function should return the continuation of
the quadratic sequence of the length equal to the length of the given list.

### Examples

    quad_sequence([48, 65, 84]) ➞ [105, 128, 153]
    
    quad_sequence([0, 1, 6, 15, 28]) ➞ [45, 66, 91, 120, 153]
    
    quad_sequence([9, 20, 33, 48]) ➞ [65, 84, 105, 128]

### Notes

Both positive and negative numbers are included in the test cases.

"""

def quad_sequence(lst):
​
  class Quad:
​
    def __init__(self, seq):
      self.s = seq
      self.l = len(seq)
      self.dif = seq[-1] - seq[-2]
      self.dif_chan = (seq[-1] - seq[-2]) - (seq[-2] - seq[-3])
    
    def advance(self):
      to_add = self.s[-1] + (self.dif + self.dif_chan)
      self.s.append(to_add)
      self.dif = self.s[-1] - self.s[-2]
      return to_add
  
  sequence = Quad(lst)
  continuation = []
​
  for n in range(sequence.l):
    continuation.append(sequence.advance())
  
  return continuation

