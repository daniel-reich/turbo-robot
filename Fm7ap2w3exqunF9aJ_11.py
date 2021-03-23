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
  n_str = str(n)
  for i in range(0, len(str(n))):
    if len(n_str) > 1:
      if int(n_str[i]) == 1:
        if i == 0 and int(n_str[i+1]) != 1:
          count += 1
        elif i + 1 == len(n_str) and int(n_str[i-1]) != 1:
          count += 1
        elif int(n_str[i-1]) != 1 and int(n_str[i+1]) != 1:
          count += 1
    else:
      count += n_str.count('1')
  return count

