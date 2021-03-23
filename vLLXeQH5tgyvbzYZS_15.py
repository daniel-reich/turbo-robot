"""


A Pythagorean triple is a set of three integer numbers that form a right
triangle. The sum of the squares of the two smaller numbers should equal the
square of the largest number. Given three numbers a, b and c (c being the
largest):

    a^2 + b^2 = c^2

Furthermore, a Pythagorean triple is said to be primitive if the three numbers
are pairwise coprime - that is, the greatest common prime factor between any
two numbers is 1.

Create a function that takes a list of three numbers (unordered) and returns
`True` if the numbers constitute a primitive Pythagorean triple, `False`
otherwise.

### Examples

    is_prim_pyth_triple([4, 5, 3]) ➞ True
    
    is_prim_pyth_triple([7, 12, 13]) ➞ False
    
    is_prim_pyth_triple([39, 15, 36]) ➞ False
    # Pythagorean triple, but not primitive.
    
    is_prim_pyth_triple([77, 36, 85]) ➞ True

### Notes

N/A

"""

def is_prim_pyth_triple(lst):
    srt = list(sorted([i**2 for i in lst]))
    if srt[0] + srt[1] != srt[2]:
         return False
    lst2 = []
    for num in lst:
        a = primes(num)
        lst2 += a
    return len(set(lst2)) == len(lst2)
​
def primes(n):
    lst,lst2 = [i for i in range(2,n) if n % i == 0],[]
    for i in lst:
        if isprime(i):
            lst2.append(i)
    return lst2
​
def isprime(n):
    z = 2
    while z < n:
        if n % z == 0:
            return False
        z += 1
    return True

