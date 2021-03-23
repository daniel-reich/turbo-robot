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
  factors = [i for i in range(2,num//2+1) if num%i==0]
  prime = [i for i in factors if all([i%j!=0 for j in range(2,i)])]
  res = []
  for i in prime:
    while num%i==0:
      res.append(i)
      num /= i
  return res

