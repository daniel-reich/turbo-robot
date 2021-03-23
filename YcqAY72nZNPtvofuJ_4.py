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

def quad_sequence(seq):
    '''
    Returns a list of the next n items of the quadratic sequence seq, where
    n is the length of n.
    '''
    # Uses the formula: ith item = Ai^2 + Bi + C where A, B and C are constants
    # and i is numbered from 1
    A = (seq[2] - seq[1] - seq[1] + seq[0])//2
    d1, d2 = seq[0] - A, seq[1] - 4 * A  # n1 - A(1^2), n2 - A(2^2)
    B, C = d2 - d1, 2 * d1 - d2
    
    return [A * i**2 + B * i + C for i in range(len(seq)+1, 2*len(seq)+1)]

