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
  def cf(x,y):
    return [i for i in range(2,min(x,y)+1) if not (x%i or y%i)]
    
  return ["0/1"] + \
  sorted(["{}/{}".format(x,y) for x in range(1,n) for y in range(1,n+1) if x<y and not cf(x,y)],key=eval) \
  + ["1/1"]

