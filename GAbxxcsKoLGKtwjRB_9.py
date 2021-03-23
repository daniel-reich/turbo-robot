"""


Create a function that takes a list of numbers and returns the **sum** of all
**prime numbers** in the list.

### Examples

    sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17
    
    sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
    
    sum_primes([]) ➞ None

### Notes

  * Given numbers won't exceed 101.
  * A prime number is a number which has exactly two divisors.

"""

def is_prime(x):
  toggle=1
  if x==1 or x==4:
    return False
  for i in range(2,x//2):
    if x%i==0:  
      toggle=0
  return bool(toggle)
​
def sum_primes(lst):
  return sum([i for i in lst if is_prime(i)]) if len(lst)>0 else None

