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

def sum_primes(lst):
    if len(lst) != 0:
        res = 0
        for x in lst:
            f_count = 0
            for i in range(1, x):
                if x % i == 0:
                    f_count += 1
            if f_count == 1:
                res += x
        return res
    else:
        return None

