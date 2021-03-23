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

def isPrime(num):
    prime = [2, 3]
    if num in prime:
        return True
    if num<2:
        return False
    for i in range(2, (num+2)//2):
        if num%i ==0:
            return False
    return True
​
def sum_primes(lst):
  if len(lst)==0:
    return None
  lst_index = list(map(isPrime, lst))
  result = [k for i, k in enumerate(lst) if lst_index[i]]
  return sum(result)

