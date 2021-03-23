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

def farey(n):
  def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)
  def hdiv(x):
    d = list(map(int, x.split('/')))
    if d[0] == 0 or d[0] == d[1]:
      return d[1] == 1
    return gcd(d[0], d[1]) == 1
  r = [str(x) + '/' + str(y) for x in range(n) for y in range(1, n + 1) if x <= y]
  return list(filter(hdiv, sorted(r, key = eval)))

