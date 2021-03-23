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
  parts = [ [ str(n)[0] ] ]
  for i in str(n)[1:]:
    if i in parts[-1]: parts[-1] += i
    else: parts.append([i])
  return sum(1 for p in parts if p == ['1'])

