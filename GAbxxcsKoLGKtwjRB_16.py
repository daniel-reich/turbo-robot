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
  sum = 0
  if len(lst)!=0:
    for num in lst:
      if num==2:
        sum += num
      elif num==1:
        continue
      else:
        for i in range(2,num):
          if num%i==0:
            break
        else:
          sum += num
    return sum
  else:
    return None

