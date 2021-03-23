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
    count1 = 0
    if lst != []:
        for i in lst:
            if i > 1:
                for j in range(2,i):
                    if (i%j)==0:
                        break
                else:
                    count1 += i
            else:
                pass
        return count1
    else:
        return None

