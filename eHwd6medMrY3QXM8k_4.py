"""


Write a function that will return `True` if a given string (divided and
grouped into a size) will contain a set of **consecutive** numbers (regardless
of orientation: whether **ascending** or **descending** ), otherwise, return
`False`.

### Examples

    is_consecutive("121314151617") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 2's : 12, 13, 14, 15, 16, 17
    
    is_consecutive("123124125") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 3's : 123, 124, 125
    
    is_consecutive("32332432536") ➞ False
    # Regardless of the grouping size, the numbers can't be consecutive.
    
    is_consecutive("326325324323") ➞ True
    # Contains a set of consecutive descending numbers
    # if grouped into 3's : 326, 325, 324, 323
    
    is_consecutive("667666") ➞ True
    # Consecutive descending numbers: 667 and 666.
    
    is_consecutive("999897959493") ➞ False

### Notes

  * A **number** can consist of any number of digits, so long as the numbers are **adjacent** to each other, and the string has **at least two** of them.
  * A **recursive** version of this challenge can be found via this [link](https://edabit.com/challenge/Ym27MyQQMRWGvEGeP).

"""

class Sequence:
  
  def __init__(self, sequence):
    self.seq = sequence
    self.is_consec = True
    
    direct = None
    
    for n in range(len(self.seq) - 1):
      ci = self.seq[n]
      ni = self.seq[n+1]
      
      if ni not in [ci + 1, ci - 1]:
        self.is_consec = False
        break
      if direct == None:
        if ni == ci + 1:
          direct = 'a'
        else:
          direct = 'd'
      elif direct == 'a':
        if ci + 1 != ni:
          self.is_consec = False
          break
      else:
        if ci - 1 != ni:
          self.is_consec = False
          break
​
def is_consecutive(s):
  print(s)
  def sequence_creator(string, size):
    sequence = []
    string = list(string)
    
    for n in range(0, len(string), size):
      nn = ''
      for x in range(size):
        try:
          nn += string[0]
        except IndexError:
          return Sequence([0,-3])
        string.pop(0)
      sequence.append(int(nn))
    
    if len(string) != 0:
      sequence.append(int(string))
      del string
    
    return Sequence(sequence)
  
  sequences = []
  half_size = len(s) // 2 + 2
  
  for n in range(1, half_size):
    sequences.append(sequence_creator(s,n))
  
  return 0 < len([sequence for sequence in sequences if sequence.is_consec == True])

