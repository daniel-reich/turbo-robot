"""


Write a function that receives a list of _x_ integers and returns a list of
_x_ integers in the Nth term of a quadratic number sequence (where _x_ is the
length of the incoming list). Your function should return the continuation of
the quadratic sequence of the length equal to the length of the given list.

### Examples

    quad_sequence([48, 65, 84]) ➞ [105, 128, 153]
    
    quad_sequence([0, 1, 6, 15, 28]) ➞ [45, 66, 91, 120, 153]
    
    quad_sequence([9, 20, 33, 48]) ➞ [65, 84, 105, 128]

### Notes

Both positive and negative numbers are included in the test cases.

"""

def quad_sequence(x):
    a = 0.5 * x[0] - x[1] + 0.5 * x[2]
    b = -2.5 * x[0] + 4 * x[1] - 1.5 * x[2]
    c = 3 * x[0] - 3 * x[1] + x[2]
    return [int(a * i * i + b * i + c)
            for i in range(len(x) + 1, 2 * len(x) + 1)]

