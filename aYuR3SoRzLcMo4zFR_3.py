"""


In this challenge you will receive an input of the form:

    [[[[[[[[[[[]]]]]]]]]]]

In other words, a list containing a list containing a list containing... a
list containing nothing.

Your goal is to measure the depth of this list, where `[]` has a depth 1,
`[[]]` has depth of 2, `[[[]]]` has depth 3, etc.

### Examples

    measure_the_depth([]) ➞ 1
    
    measure_the_depth([[]]) ➞ 2
    
    measure_the_depth([[[]]]) ➞ 3
    
    measure_the_depth([[[[[[[[[[[]]]]]]]]]]]) ➞ 11

### Notes

One way to solve this is with recursion; but maybe there's a way to "count the
brackets"?

"""

def measure_the_depth(lst):
    cnt = 1
    while len(lst) > 0 and type(lst) == list:
        cnt += 1
        lst = lst[0]
    return cnt

