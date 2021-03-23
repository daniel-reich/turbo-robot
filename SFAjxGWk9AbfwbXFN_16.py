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
  return [i for i in range(2, n+1) if(i == 2 or i ==3 or i == 5 or i ==7) or (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0)]

