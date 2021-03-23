"""


Create a function that takes a list of integers and returns the range of
consecutive numbers separated by dash a `-` between `starting` and `ending`
numbers.

  * Separate different ranges by `,` commas.
  * A range of numbers will be considered if **three or more consecutive numbers** are found in the list (see example #1).

### Examples

    numbers_range([-6, -3, -2, -1, 0, 1, 7, 8, 9, 10, 11, 14, 15]) ➞ "-6,-3-1,7-11,14,15"
    # -6 is an alone integer.
    # -3 to 1 is a range of consecutive numbers.
    # 7 to 11 is a range of consecutive numbers.
    # 14 and 15 are consecutive numbers but cannot be considered as a range.
    
    numbers_range([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]) ➞ "-3--1,2,10,15,16,18-20"
    
    numbers_range([1, 2, 3, 9, 10, 15, 16, 18, 56, 57]) ➞ "1-3,9,10,15,16,18,56,57"

### Notes

N/A

"""

def numbers_range(ranges):
    if not ranges:
        return ''
    if len(ranges) == 1:
        return str(ranges[0])
​
    groups = [[ranges.pop(0)]]
​
    for i in ranges:
        if i - groups[-1][-1] == 1:
            groups[-1].append(i)
        else:
            groups.append([i])
            
    for idx, g in enumerate(groups):
        if len(g) >= 3:
            groups[idx] = '{}-{}'.format(g[0], g[-1])
        elif len(g) == 2:
            groups[idx] = '{}, {}'.format(g[0], g[1])
        else:
            groups[idx] = str(g[0])
            
    return ', '.join(groups)

