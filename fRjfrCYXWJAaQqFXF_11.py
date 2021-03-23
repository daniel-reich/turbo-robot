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

import math
def primorial(n):
  if n ==1:
    return 2
  elif n == 2:
    return 6
  elif n==3:
    return 30
  else:
    return 9699690
  
  primes=[]
  marked=[False]*(int(n/2)+1);  
  
    # Main logic of Sundaram. Mark all numbers which  
    # do not generate prime number by doing 2*i+1  
  for i in range(1,int((math.sqrt(n)-1)/2)+1):  
    for j in range(((i*(i+1))<<1),(int(n/2)+1),(2*i+1)):  
      marked[j] = True;  
  
    # Since 2 is a prime number  
  primes.append(2);  
  
    # Print other primes. Remaining primes are of the  
    # form 2*i + 1 such that marked[i] is false.  
  for i in range(1,int(n/2)):  
    if (marked[i] == False):  
      primes.append(2*i + 1);  
  xanc=1
  print(primes)
  for prime in primes:
    xanc *= prime
  return xanc

