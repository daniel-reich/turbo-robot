"""


Create a function that returns a list containing the prime factors of whatever
integer is passed to it.

### Examples

    prime_factors(20) ➞ [2, 2, 5]
    
    prime_factors(100) ➞ [2, 2, 5, 5]
    
    prime_factors(8912234) ➞ [2, 47, 94811]

### Notes

  * Implement your solution using trial division.
  * Your solution should not require recursion.

"""

def prime_factors(num):
    list = []
    n = num
    d = 2
    if n == 0 or n == 1:
        return 0
​
    elif n >= 2:
        while n >= d:
            if n % d == 0:
                list.append(d)
                n = n/d
            else:
                d+=1
        return list

