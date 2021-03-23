"""


Create a function that can take 1, 2, or 3 arguments (like the range function)
and returns a tuple. This should be able to return float values (as opposed to
the range function which can't take float values as a step).

### Examples

    drange(1.2, 5.9, 0.45) ➞ (1.2, 1.65, 2.1, 2.55, 3.0, 3.45, 3.9, 4.35, 4.8, 5.25, 5.7)
    
    drange(10) ➞ (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    
    drange(1, 7, 1.2) ➞ (1, 2.2, 3.4, 4.6, 5.8)
    # Here 7 is not included, like in the range function.

### Notes

Always round values to the number with the most decimal digits (e.g. in the
first example, the answer should always be rounded to 2 digits. In the second,
it should be rounded to 0 digits and the third, 1 digit).

"""

def drange(*args):
    r = []
    g = iter(args)
    a = next(g)
    b = next(g, - 1)
    c = next(g, 1)
    if b == - 1:
        a, b = 0, a
    decimals = max(deci(a), deci(b), deci(c))
    while a < b:
        r.append(round(a, decimals))
        a += c
    return tuple(r)
    
def deci(x):    
    if type(x) == float:
        return len(str(x).split(".")[1])
    return 0

