"""


Create a function that checks if the sub-lists in a list adhere to the
specified pattern.

### Examples

    check_pattern([[1, 1], [2, 2], [1, 1], [2, 2]], "ABAB") ➞ True
    
    check_pattern([[1, 2], [1, 3], [1, 4], [1, 2]], "ABCA") ➞ True
    
    check_pattern([[1, 2, 3], [1, 2, 3], [3, 2, 1], [3, 2, 1]], "AABB") ➞ True
    
    check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "ABCD") ➞ True
    
    check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "DCBA") ➞ True

### Notes

  * The length of the pattern will always be the same as the length of the (main) list.
  * The pattern does not necessarily have to be alphabetically ordered (see last example).

"""

def pat(x):
    val = 0
    vals = []
    for i in range(len(x)):
        if i == 0 or x[i] not in x[:i]:
            vals.append(val)
            val += 1
        else:
            vals.append([vals[j] for j in range(len(vals)) if x[i] == x[j]][0])
    return vals
​
def check_pattern(lst, pattern):
    return pat(lst) == pat(pattern)

