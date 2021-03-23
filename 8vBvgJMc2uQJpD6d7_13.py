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

def prime_factors(num):
  tst = [x for x in reversed(range(1,num))]
  pf =[]
  x = 0
  while (x < len(tst)):
    if (num%tst[x] == 0 and isprime(tst[x])and tst[x] != 1):
      pf.append(tst[x])
      num /= tst[x]
    else:
      x +=1
  pf.reverse()
  return pf
  
def isprime(num):
  if (num == 2):
    return True
  return not any([num%x == 0 for x in range(2,num)])

