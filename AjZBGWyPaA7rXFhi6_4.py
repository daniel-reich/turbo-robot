"""


Write a function that returns the minimum number of swaps to convert the first
binary string into the second.

### Examples

    min_swaps("1100", "1001") ➞ 1
    
    min_swaps("110011", "010111") ➞ 1
    
    min_swaps("10011001", "01100110") ➞ 4

### Notes

  * Both binary strings will be of equal length.
  * Both binary strings will have an equal number of zeroes and ones.
  * A swap is switching two elements in a string (swaps do **not** have to be adjacent).

"""

def min_swaps(s1, s2):
  count = 0
  for i, v in enumerate(s1):
    if s1[i] != s2[i]:
      count += 1
  return count/2

