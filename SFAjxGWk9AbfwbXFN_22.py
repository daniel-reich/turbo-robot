"""


Create a function that will find all primes below a given number. Return the
result as a list.

### Examples

    primes_below_num(5) ➞ [2, 3, 5]
    
    primes_below_num(10) ➞ [2, 3, 5, 7]
    
    primes_below_num(20) ➞ [2, 3, 5, 7, 11, 13, 17, 19]

### Notes

If `n` is a prime, it is included in the list.

"""

def primes_below_num(n):
  primes =[]
  for i in range(2,n+1):
    if n > 1:
      for j in range(2,i):
        if i%j == 0:
          break
      else:
        primes.append(i)
  return primes
​
print(primes_below_num(5))

