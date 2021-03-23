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

sum_primes=lambda l:sum(filter(lambda p:p>1and all(p%i for i in range(2,int(p**0.5+1))),l))or None

