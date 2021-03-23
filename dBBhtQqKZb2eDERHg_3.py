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

import math
def numberSequence(n):
    res=[]
    if n<=0:
        return '-1'
    else:
        if n%2!=0:
            n=math.ceil(n/2)
            x=[str(i) for i in range(1,n+1)]
            a=x[::-1]+x[1:]
            b=[str(x) for x in a] 
            return str(" ".join(b))
        if n%2==0:
            n=math.ceil(n/2)
            x=[str(i) for i in range(1,n+1)]
            a=x[::-1]+x
            b=[str(x) for x in a] 
            return str(" ".join(b))

