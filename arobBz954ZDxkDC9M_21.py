"""


Given an integer, create a function that returns the next prime. If the number
is prime, return the number itself.

### Examples

    next_prime(12) ➞ 13
    
    next_prime(24) ➞ 29
    
    next_prime(11) ➞ 11
    # 11 is a prime, so we return the number itself.

### Notes

N/A

"""

def next_prime(num):
    if num<2:
        return 2
    def is_prime(num):
        if num in range(2,4):
            return True
        res=[num%x for x in range(2,(num//2)+1)]
        if 0 in res:
            return False
        else:
            return True
​
    if is_prime(num):
        return(num)
    return next_prime(num+1)

