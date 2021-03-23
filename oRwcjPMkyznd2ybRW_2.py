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
    prod, numb, ans = [], [], []
    for each in range(1, n + 1):
        i = 1
        for num in str(each):
            i *= int(num)
        numb.append(each)
        prod.append(i)
    for each in range(prod.count(max(prod))):
        get_index = prod.index(max(prod))
        ans.append(numb[get_index])
        prod.remove(max(prod))
        numb.remove(numb[get_index])
    return ans

