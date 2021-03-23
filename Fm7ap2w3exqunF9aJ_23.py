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
  count = 0
  n = str(n)
  if len(n) < 3:
    return n.count('1') if n.count('1') != 2 else 0
  for i in range(len(n) - 3):
    if n[i] != '1' and n[i+1] == '1' and n[i+2] != '1':
      count += 1
  if n[0] == '1' and n[1] != '1':
    count += 1
  if (n[-1] == '1' and n[-2] != '1'):
    count += 1
  return count

