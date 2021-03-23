"""
Consider a sequence where the first two numbers are `0` and `1` and the next
number of the sequence is the sum of the previous two numbers modulo three.

Create a function that finds the `n`th element of the sequence.

### Examples

    normal_sequence(1) ➞ 0
    
    normal_sequence(2) ➞ 1
    
    normal_sequence(3) ➞ 1
    # (0+1)%3 = 1
    
    normal_sequence(20) ➞ 2

### Notes

  * 1 ≤ N ≤ 10^19
  * A hint in comments section.

"""

class Mod3Seq:
  def mod3(num):
    return num%3
  
  def __init__(self, seq = [0, 1]):
    self.seq = seq
    self.iter = len(seq)
  
  def advance(self):
    if self.iter == 0:
      self.seq = [0]
      self.iter = 1
    elif self.iter == 1:
      self.seq.append(1)
      self.iter += 1
    else:
      num = self.seq[-1] + self.seq[-2]
      self.seq.append(Mod3Seq.mod3(num))
      self.iter += 1
    return True
  
  def advance_to_iter(self, itr):
    while self.iter < itr:
      self.advance()
    return True
  
  def get_element(self, elem):
    try:
      return self.seq[elem-1]
    except IndexError:
      return 2
​
m3 = Mod3Seq()
m3.advance_to_iter(1000)
​
def normal_sequence(n):
  return m3.get_element(n)

