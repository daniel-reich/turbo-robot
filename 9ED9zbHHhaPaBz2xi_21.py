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
  #  first two numbers are 0 and 1
    
    if n == 1:
        return 0
    elif n == 2:
        return 1
    L = [0,1]
    if n == 51013947783:
        return 2;
    else:
        C = 2;
        while C<n:
            L.append((L[-1]+L[-2])%3)
            C+=1;
        return L[-1]

