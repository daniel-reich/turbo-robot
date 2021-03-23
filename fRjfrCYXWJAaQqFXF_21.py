"""


A _Primorial_ is a product of the first `n` prime numbers (e.g. `2 x 3 x 5 =
30`). `2, 3, 5, 7, 11, 13` are prime numbers. If `n` was `3`, you'd multiply
`2 x 3 x 5 = 30` or Primorial = `30`.

Create a function that returns the Primorial of a number.

### Examples

    primorial(1) ➞ 2
    
    primorial(2) ➞ 6
    
    primorial(8) ➞ 9699690

### Notes

N/A

"""

import functools
def primorial(n):
    res = []
    i=2
    while(len(res)!=n):
        if i>1:
            for j in range(2,i):
                if(i % j==0):break
            else:res.append(i)
        i+=1
    return  functools.reduce(lambda x,y:x*y, res)

