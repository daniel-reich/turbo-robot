"""


Given a list of integers `lst`, return the **sum of all the integers** that
have _an even index, multiplied by the integer at the last index_.

If the sequence is empty, you should return `0`.

### Examples

    even_last([2, 3, 4, 5]) ➞ 30
    # numbers at even index = 2, 4
    # number at last index = 5
    # 2*5 + 4*5 = 10 + 20 = 30
    
    even_last([1, 3, 3, 1, 10]) ➞ 140
    
    even_last([]) ➞ 0

### Notes

N/A

"""

def even_last(lst):
    count = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            count += lst[i]
    if lst:
        return count * lst[-1]
    elif not lst:
        return 0

