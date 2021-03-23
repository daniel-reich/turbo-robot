"""


Create a function that counts the number of blocks of **two or more** adjacent
`1`s in a list.

### Examples

    count_ones([1, 0, 0, 1, 1, 0, 1, 1, 1]) ➞ 2
    # Two instances: [1, 1] (middle) and [1, 1, 1] (end)
    
    count_ones([1, 0, 1, 0, 1, 0, 1, 0]) ➞ 0
    
    count_ones([1, 1, 1, 1, 0, 0, 0, 0]) ➞ 1
    
    count_ones([0, 0, 0]) ➞ 0

### Notes

  * A single 1 by itself (surrounded by a zero on its left and right), does **not** count towards the total (see first example).
  * Each input will contain only zeroes and ones.

"""

def count_ones(lst):
  count = 0
  if lst[0] == 1 and lst[1] == 1:
    count += 1
  for i in range(1,len(lst)-1):
    if lst[i]==1:
      if lst[i-1] != 1 and lst[i+1] == 1:
        count += 1
  return count

