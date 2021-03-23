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

def numberSequence(n, d = 1, ans = ''):
    if n <= 0: return '-1'
    if d == 1:
        ans = '1' if n%2 else '1 1'
    else:
        ans = str(d) + ' ' + ans + ' ' + str(d)
    return ans if n == (len(ans) + 1)//2 else numberSequence(n, d + 1, ans)

