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

import numpy as np
​
def is_prime(x):
  for i in range(2,x):
    if (x % i) ==0:
      return False
      break
            
  else:
    return True
        
​
def primorial(x):
  l = [2]
  y = 3
  a = 1
    
  while len(l) < x:
    if is_prime(y):
      l.append(y)
    y+=1
        
    
    
  return np.prod(l)

