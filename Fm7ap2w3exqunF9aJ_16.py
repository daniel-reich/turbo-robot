"""


Create a function which counts how many lone `1`s appear in a given number.
Lone means the number doesn't appear twice or more in a row.

### Examples

    count_lone_ones(101) ➞ 2
    
    count_lone_ones(1191) ➞ 1
    
    count_lone_ones(1111) ➞ 0
    
    count_lone_ones(462) ➞ 0

### Notes

Tests will include positive whole numbers only.

"""

def count_lone_ones(n):
    str1 = str(n)
    lst1 = [i * '1' for i in range(2, len(str1) + 1)]
    for i in lst1[::-1]: str1 = str1.replace(i, '')
    return list(str1).count('1')

