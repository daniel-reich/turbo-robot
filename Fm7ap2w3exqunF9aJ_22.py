"""


Create a function which counts how many lone `1`s appear in a given number.
Lone means the number doesn't appear twice or more in a row.

### Examples

    count_lone_ones(101) ➞ 2
    
    count_lone_ones(1191) ➞ 1
    
    count_lone_ones(1111) ➞ 0
    
    count_lone_ones(462) ➞ 0

### Notes

Tests will include positive whole numbers only.

"""

def count_lone_ones(n):
  p = [int(i) for i in list(str(n))]
  o = [0]+p+[0]
  return len([o[i] for i in range(len(o)) if o[i] == 1 and o[i-1] != 1 and o[i+1] != 1])

