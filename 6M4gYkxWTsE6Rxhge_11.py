"""


Create a function thats takes a list and returns `True` if every number is
prime. Otherwise, return `False`.

### Examples

    all_prime([7, 5, 2, 4, 6]) ➞ False
    
    all_prime([2, 3, 5, 7, 13, 17, 19, 23, 29]) ➞ True
    
    all_prime([1, 5, 3]) ➞ False

### Notes

1 is not a prime number.

"""

def all_prime(lst):
  def prime(n):
    return all([(n%j) for j in range(2,int(n**0.5)+1)]) and n>1
  result = list(map(prime,lst))
  return True if len(list(set(result))) == 1 else False

