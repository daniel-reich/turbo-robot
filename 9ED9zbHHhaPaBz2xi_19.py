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

seq = [0, 1]
a, b = 0, 1
while True:
    a, b = b, (a + b) % 3
    seq.append(b)
    if seq[-2:] == [0, 1]:
        break
        
def normal_sequence(n):
    return seq[n % 8 - 1]

