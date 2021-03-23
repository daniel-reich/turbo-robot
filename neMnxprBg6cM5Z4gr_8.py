"""


In mathematics, an **Arithmetic Progression (AP)** is a sequence of numbers
such that the difference between the consecutive terms is constant. Create a
function that takes three arguments:

  * The first element of the sequence `first`
  * Constant difference between the elements `diff`
  * Total numbers in the sequence `n`

Return the first `n` elements of the sequence with the given common difference
`diff`. Final result should be a string of numbers, separated by comma and
space.

### Examples

    arithmetic_progression(1, 2, 5) ➞ "1, 3, 5, 7, 9"
    
    arithmetic_progression(1, 0, 5) ➞ "1, 1, 1, 1, 1"
    
    arithmetic_progression(1, -3, 10) ➞ "1, -2, -5, -8, -11, -14, -17, -20, -23, -26"

### Notes

N/A

"""

def arithmetic_progression(start, diff, n):
  seq = [start]
  for i in range(n-1):
    seq.append(seq[i]+diff)
  return ', '.join(str(i) for i in seq)

