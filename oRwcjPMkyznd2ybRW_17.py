"""


Write a function that returns all numbers **less than or equal to N** with the
maximum product of digits.

### Examples

    max_product(8) ➞ [8]
    
    max_product(27) ➞ [27]
    
    max_product(211) ➞ [99, 199]
    
    max_product(9578) ➞ [8999]

### Notes

Search for numbers in the range: `[0, n]`.

"""

def max_product(n):
    lst, lstnums, res, num = [], [], [], 1
    for i in range(0, n+1):
        lstnums.append(i)
        for j in str(i):
            num *= int(j)
        lst.append(num)
        num = 1
​
    maxlst = max(lst)
    for i in range(len(lst)):
        if lst[i] == maxlst:
            res.append(lstnums[i])
​
    return res

