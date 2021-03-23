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

def is_prime(n):
    return True if n == 2 else False if n == 1 else all(n % num != 0 for num in range(2, n))
​
def all_prime(nums):
    return all(is_prime(x) for x in nums)

