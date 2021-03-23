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

def numberSequence(n, odd=True, res=None):
    if res is None:
        if n < 1:
            return '-1'
        if n == 1:
            return '1'
        if n == 2:
            return '1 1'
        odd = n % 2
        if odd:
            n = (n + 1) // 2
        else:
            n //= 2
        res = '{}'.format(n)
        n -= 1
    if n > 1:
        res += ' {}'.format(n)
    elif n == 1:
        if odd:
            return res + ' 1 ' + res[::-1]
        else:
            return res + ' 1 1 ' + res[::-1]
    return numberSequence(n - 1, odd, res)

