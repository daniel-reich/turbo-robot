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

def numberSequence(n, s = 1, r = None, t = None):
    if not t:
        if n < 3 : return "1" + " 1"*(n == 2) if n > 0 else "-1"
        n, r = int(-1 * (n / 2) // 1 * -1), (n - 1) % 2; t = n
    if s:
        return " "*(t!=n)+str(n)+numberSequence(n - 1, s, r, t) if n > 1 else " 1"*(1+r) + numberSequence(n + 1, 0, r, t)
    else:
        return " "+str(n)+numberSequence(n + 1, s, r, t) if n <= t else ""

