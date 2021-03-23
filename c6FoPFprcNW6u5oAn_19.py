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
  lst = [[0,"0/1"], [1, "1/1"]]
  for i in range(2, n+1):
    for j in range(1, i):
      if not  j/i in [x[0] for x in lst]:
        lst.append([j/i, "{}/{}".format(j,i)])
  lst.sort()
  return [x[1] for x in lst]

