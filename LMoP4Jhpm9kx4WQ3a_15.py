"""


Write a function that will return `True` if a given string (divided and
grouped into a size) will contain a set of **consecutive ascending** numbers,
otherwise, return `False`.

### Examples

    is_ascending("123124125") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 3's : 123, 124, 125
    
    is_ascending("101112131415") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 2's : 10, 11, 12, 13, 14, 15
    
    is_ascending("32332432536") ➞ False
    # Regardless of the grouping size, the numbers can't be consecutive.
    
    is_ascending("326325324323") ➞ False
    # Though the numbers (if grouped into 3's) are consecutive but descending.
    
    is_ascending("666667") ➞ True
    # Consecutive numbers: 666 and 667.

### Notes

  * A **number** can consist of any number of digits, so long as the numbers are **adjacent to each other** , and the string has **at least two** of them.
  * A **recursive** version of this challenge can be found via this [link](https://edabit.com/challenge/Pjffmm9TTr7CxGDRn).

"""

class Sequence:
​
  def __init__(self, start):
    self.start = start
    self.seq = [int(start)]
  
  def advance(self):
    self.seq.append(max(self.seq) + 1)
    return True
  
  def match(self, string):
    
    curr = ''.join([str(i) for i in self.seq])
    while len(curr) < len(string):
      self.advance()
      curr = ''.join([str(i) for i in self.seq])
    
    return curr == string
​
def is_ascending(s):
  
  sequences = []
  
  for n in range(1, len(s) // 2 + 1):
    sequences.append(Sequence(s[:n]))
  
  for sequence in sequences:
    if sequence.match(s) == True:
      return True
  
  return False

