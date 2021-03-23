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
  seq = [0,1]
  for i in range(n-1):
    if len(seq)<8:
      seq.append((seq[-1]+seq[-2])%3)
    else:
      return seq[(n%8)-1]
  return seq

