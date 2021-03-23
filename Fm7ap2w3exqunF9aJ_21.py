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

import re
def count_lone_ones(n):
    num=str(n)
    pattern = re.compile(r'(1){2,20}')
    matches = pattern.finditer(num)
    k = "".join(i.group(0) for i in matches)
    return num.count("1")-len(k)

