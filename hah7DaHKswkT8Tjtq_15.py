"""


A numeric string `s` is beautiful if it can be split into a sequence of two or
more positive integers, `a[1]`, `a[2]`, `...a[n]`, satisfying the following
conditions:

  1. `a[i] - a[i-1] = 1` for any `1 < i <= n` (i.e. each element in the sequence is one more than the previous element).
  2. No `a[i]` contains a leading zero. For example, we can split `s = 10203` into the sequence `{1, 02, 03}`, but it is not beautiful because `02` and `03` have leading zeroes.
  3. The contents of the sequence cannot be rearranged. For example, we can split `s = 312` into the sequence `{3, 1, 2}`, but it is not beautiful because it breaks our first constraint (i.e. `1 - 3 ≠ 1`).

Return either `"YES x"` where `x` is the smallest first number of the
increasing sequence or `"NO"` if there is no valid sequence.

### Examples

    separate_numbers("1234") ➞ "YES 1"
    
    separate_numbers("91011") ➞ "YES 9"
    
    separate_numbers("99100") ➞ "YES 99"
    
    separate_numbers("101103") ➞ "NO"
    
    separate_numbers("010203") ➞ "NO"

### Notes

N/A

"""

def separate_numbers(s):
​
  class Sequence:
​
    def rule_1(numbers):
​
      for n in range(1, len(numbers)):
        ci = numbers[-n]
        try:
          ni = numbers[-(n+1)]
        except IndexError:
          print(ci, n)
        if ci - ni != 1:
          return False
      
      return True
    
    def rule_2(numbers):
​
      for num in numbers:
        if num[0] == '0':
          return False
​
      return True
​
    def __init__(self, start):
      self.start = start
      self.seq = [int(start)]
    
    def advance(self):
      self.seq.append(max(self.seq) + 1)
      return True
    
    def match(self, string):
      curr = ''.join([str(s) for s in self.seq])
      while len(curr) < len(string):
        self.advance()
        curr = ''.join([str(s) for s in self.seq])
      
      return curr == string and len(self.seq) > 1
    
    def valid(self):
      return Sequence.rule_1(self.seq) == Sequence.rule_2([str(s) for s in self.seq]) == True
  
  sequences = []
​
  for n in range(1, len(s)//2 + 2):
    sequences.append(Sequence(s[:n]))
​
  for sequence in sequences:
    if sequence.match(s) == True:
   #   print(sequence.seq, sequence.start, s)
      return 'YES ' + sequence.start
  
  return 'NO'

