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

def quad_sequence(lst):
    n = len(lst)
    diff1 = [lst[i] - lst[i-1] for i in range(1, n)]
    diff2 = [diff1[i] - diff1[i-1] for i in range(1, n - 1)]
    assert len(set(diff2)) == 1
    a = diff2[0] // 2
    subs = [(lst[k - 1] - a * k**2) for k in range(1, n + 1)]
    diff3 = [subs[i] - subs[i-1] for i in range(1, len(subs))]
    assert len(set(diff3)) == 1, diff3
    b = diff3[0]
    c = lst[0] - a - b #b + diff3[0]#subs[0] - lst[0]
    ans = [a*k**2 + b*k + c for k in range(n + 1, 2 * n + 1)]
    return ans

