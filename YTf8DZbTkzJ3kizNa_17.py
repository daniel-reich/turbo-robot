"""
A **Harshad** number is a number which is divisible by the sum of its digits.
For example, 132 is divisible by 6 (1+3+2).

A subset of the Harshad numbers are the **Moran** numbers. Moran numbers yield
a prime when divided by the sum of their digits. For example, 133 divided by 7
(1+3+3) yields 19, a prime.

Create a function that takes a number and returns `"M"` if the number is a
Moran number, `"H"` if it is a (non-Moran) Harshad number, or `"Neither"`.

### Examples

    moran(132) ➞ "H"
    
    moran(133) ➞ "M"
    
    moran(134) ➞ "Neither"

### Notes

N/A

"""

def is_prime(m):
    lista = list(range(2, m))
    for i in lista:
​
        if m % i==0:
​
            return False
    return True
​
​
def moran(n):
    con=list((str(n)))
    ana=sum((int(i)) for i in con)
    ar=int(n/ana)
    if is_prime(ar)==True:
        return "M"
    elif n%ana==0:
        return "H"
​
    else:
        return "Neither"

