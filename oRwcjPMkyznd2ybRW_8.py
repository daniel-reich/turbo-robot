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
    result = [(0, 0)]
    for i in range(0, n + 1):
        n = [int(x) for x in str(i)] 
        add = 1
        for j in n:
            add = add * int(j)
        if add > result[0][0]:
            result = [(add, i)]
        elif add == result[0][0]:
            result.append((add, i))
    return [i[1] for i in result]

