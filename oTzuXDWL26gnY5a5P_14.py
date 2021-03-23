"""


Create a function that finds how many prime numbers there are, up to the given
integer.

### Examples

    prime_numbers(10) ➞ 4
    # 2, 3, 5 and 7
    
    prime_numbers(20) ➞ 8
    # 2, 3, 5, 7, 11, 13, 17 and 19
    
    prime_numbers(30) ➞ 10
    # 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29

### Notes

N/A

"""

def isprime(num):
    if num < 2:
        return False
    elif num < 4:
        return True
    for x in range(2, num-1):
        if num // x == num / x:
            return False
    return True
​
def prime_numbers(num):
    return sum([1 if isprime(x) else 0 for x in range(num)])

