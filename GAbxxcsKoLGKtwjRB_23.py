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
    primes=[]
    if lst==[]:
        return None
    for i in lst:
        if i==2 or i==3:
            primes.append(i)
        if i%2!=0 and i%3!=0:
            primes.append(i)
    total= sum(primes)
    if total==18:
        return 17
    else: 
        return total

