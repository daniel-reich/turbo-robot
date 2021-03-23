"""


Write a **recursive** function that accepts an integer `n` and return a
sequence of `n` integers as a string, descending from `n` to 1 and then
ascending back from 1 to `n` as in the examples below:

### Examples

    number_sequence(1) ➞ "1"
    
    number_sequence(2) ➞ "1 1"
    
    number_sequence(3) ➞ "2 1 2"
    
    number_sequence(4) ➞ "2 1 1 2"
    
    number_sequence(9) ➞ "5 4 3 2 1 2 3 4 5"
    
    number_sequence(10) ➞ "5 4 3 2 1 1 2 3 4 5"

### Notes

  * Only use recursion.
  * No auxiliary data structures like list and tuple are allowed.

"""

def numberSequence(n):
  if n <= 0:
    return "-1"
  elif n == 1:
    return "1"
  elif n % 2 == 1:
    k = str(int(numberSequence(n-1)[0])+1) + " " + numberSequence(n-1)[:numberSequence(n-1).index("1")]
    return k + "1" + k[::-1]
  else:
    k = numberSequence(n-1)[:numberSequence(n-1).index("1")+1]
    return k + " " + k[::-1]

