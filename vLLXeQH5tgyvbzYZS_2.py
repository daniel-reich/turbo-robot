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

def gcd(a,b):
    if a==0:
        return b
    else :
        return gcd(b%a,a)
def is_prim_pyth_triple(lst):
    lst.sort()
    return lst[0]**2+lst[1]**2==lst[2]**2 and gcd(lst[0],lst[1])==1

