"""


Write a function that finds the **largest even number** in a list. Return `-1`
if not found. The use of built-in functions `max()` and `sorted()` are
prohibited.

### Examples

    largest_even([3, 7, 2, 1, 7, 9, 10, 13]) ➞ 10
    
    largest_even([1, 3, 5, 7]) ➞ -1
    
    largest_even([0, 19, 18973623]) ➞ 0

### Notes

Consider using the **modulo operator** `%` or the **bitwise and operator**
`&`.

"""

def largest_even(lst):
    ans = [x for x in lst if x % 2 == 0]
    i = 0
    if ans == []:
        return -1
    else:
        done = [ans[i]]
    while len(ans)>(i+1):
        if ans[i] < ans[i+1]:
            done = [ans[i+1]]
        ans = ans[1:]
        i += 1
    return done[0]

