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

def count_lone_ones(n: int) -> int:
    ans, n_str = 0, str(n)
    if len(n_str) == 1:
        if n == 1:
            return 1
        else:
            return 0
    for i, val in enumerate(n_str):
        if i == 0 and val == '1' and n_str[i+1] != '1':
            ans += 1
        elif i == len(n_str) - 1 and val == '1' and n_str[i-1] != '1':
            ans += 1
        elif i != 0 and i != len(n_str) - 1 and val == '1' and n_str[i+1] != '1' and n_str[i-1] != '1':
            ans += 1
    return ans

