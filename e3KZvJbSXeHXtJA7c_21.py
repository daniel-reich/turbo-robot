"""


Create a function that returns the sum of missing numbers.

### Examples

    sum_missing_numbers([1, 3, 5, 7, 10]) ➞ 29
    # 2 + 4 + 6 + 8 + 9
    
    sum_missing_numbers([10, 7, 5, 3, 1]) ➞ 29
    
    sum_missing_numbers([10, 20, 30, 40, 50, 60]) ➞ 1575

### Notes

The minimum and maximum value of the given list are the inclusive bounds of
the numeric range to consider when searching for missing numbers.

"""

def sum_missing_numbers(lst):
    lst.sort()
    total = 0
    for n in range(lst[0], lst[-1]):
        if n not in lst:
            total += n
    return total

