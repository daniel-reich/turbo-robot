"""
Consider a sequence where the first two numbers are `0` and `1` and the next
number of the sequence is the sum of the previous two numbers modulo three.

Create a function that finds the `n`th element of the sequence.

### Examples

    normal_sequence(1) ➞ 0
    
    normal_sequence(2) ➞ 1
    
    normal_sequence(3) ➞ 1
    # (0+1)%3 = 1
    
    normal_sequence(20) ➞ 2

### Notes

  * 1 ≤ N ≤ 10^19
  * A hint in comments section.

"""

def normal_sequence(n):
  rem = n % 8
  if rem in (1, 5):
    return 0
  elif rem in (2, 3, 0):
    return 1
  return 2

