"""


Create a function that returns a list containing the prime factors of whatever
integer is passed to it.

### Examples

    prime_factors(20) ➞ [2, 2, 5]
    
    prime_factors(100) ➞ [2, 2, 5, 5]
    
    prime_factors(8912234) ➞ [2, 47, 94811]

### Notes

  * Implement your solution using trial division.
  * Your solution should not require recursion.

"""

import math 
def prime_factors(n):
    pfLst=[]
    while n % 2 == 0: 
        pfLst.append(2)
        n = n / 2
​
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            pfLst.append(i)
            n = n / i
    if n>2:
        pfLst.append(int(n))
    return pfLst

