"""


Create a function that returns the _nth_ row of [Pascal's
triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle):

![Pascals triangle](https://edabit-
challenges.s3.amazonaws.com/23050fcb53d6083d9e42043bebf2863fa9746043.svg)

### Examples

    pascal_row(0) ➞ [1]
    
    pascal_row(1) ➞ [1, 1]
    
    pascal_row(5) ➞ [1, 5, 10, 10, 5, 1]
    
    pascal_row(10) ➞ [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]

### Notes

Input will include large numbers (the formula _n choose k_ , or
`n!/(k!*(n-k)!)` won't do).

"""

def pascal_row(n):
    r = [1]
    if n == 0:
        return r
    for i in range(1, n):
        add = r[-1] * (n + 1 - i) // i
        r.append(add)
    return r + [1]

