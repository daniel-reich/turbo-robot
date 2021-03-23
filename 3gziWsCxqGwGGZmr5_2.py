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

def fat_prime(a, b):
    for i in reversed(range(min(a,b),max(a,b)+1)):
        if is_prime(i):
            return i;
    
    
def is_prime(n):
    C = 0;
    N = n;
    while N != 0:
        if n % N == 0:
            C+=1;
        N-=1;
    if C ==2:
        return True
    return False

