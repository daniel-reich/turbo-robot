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
    diff_1 = lst[1] - lst[0]
    diff_2 = lst[2] - lst[1]
    quad_diff = (diff_2 - diff_1)
    last_diff = lst[-1] - lst[-2]
​
    copy = list(lst)
    i = 0
    while i < len(lst):
        copy.append(copy[-1]+last_diff+(i+1)*quad_diff)
        i += 1
    return copy[len(lst):len(copy)]

