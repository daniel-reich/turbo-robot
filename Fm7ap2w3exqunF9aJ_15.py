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
    n = str(n)
    for x in range(len(n), 1, -1):
        n = n.replace(x * "1", "_")
    return n.count("1")

