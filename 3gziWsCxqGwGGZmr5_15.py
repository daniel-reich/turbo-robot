"""


Given two integers as arguments, create a function that finds the largest
prime within the range of the two integers.

### Examples

    fat_prime(2, 10) ➞ 7
    # range [2, 3, 4, 5, 6, 7, 8, 9, 10] and the largest prime is 7.
    
    fat_prime(10, 2) ➞ 7
    # [10, 9, 8, 7, 6, 5, 4, 3, 2] and the largest prime is 7.
    
    fat_prime(4, 24) ➞ 23
    # range [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] the largest prime is 23.

### Notes

All numbers will be positive integers.

"""

is_prime = lambda n: n > 1 and all(n%i for i in range(2, int(n**0.5 + 1)))
​
def fat_prime(a, b):
    '''
    Returns the largest prime in the range (a, b) where a and b are +ve integers
    '''
    for i in range(max(a,b),min(a,b)-1,-1):
        if is_prime(i):
            return i
​
    return "Ooer! There ain't one in this range!!"

