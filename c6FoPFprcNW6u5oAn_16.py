"""


The Farey sequence of order `n` is the set of all fractions with a denominator
between 1 and `n`, reduced and returned in ascending order. Given `n`, return
the Farey sequence as a list, with each fraction being represented by a string
in the form "numerator/denominator".

### Examples

    farey(1) ➞ ["0/1", "1/1"]
    
    farey(4) ➞ ["0/1", "1/4", "1/3", "1/2", "2/3", "3/4", "1/1"]
    
    farey(5) ➞ ["0/1", "1/5", "1/4", "1/3", "2/5", "1/2", "3/5", "2/3", "3/4", "4/5", "1/1"]

### Notes

The Farey sequence will always begin with "0/1" and end with "1/1".

"""

def farey(s):
  gcd, f = lambda a, b: gcd(b, a % b) if b else a, []
  for d in range(s, 1, -1):
    for n in range(1, d):
      if gcd(n, d) == 1: f += ['{}/{}'.format(n, d)]
  return sorted(['0/1']+f+['1/1'], key=lambda x: eval(x))

