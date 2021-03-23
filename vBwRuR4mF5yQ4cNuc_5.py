"""


Create a function that takes a list of "mostly" numbers, counts the amount of
missing numbers and returns their sum. Watch out for strings!

### Examples

    count_missing_nums(["1", "3", "5", "7", "9"]) ➞ 4
    # 1+1+1+1
    
    count_missing_nums(["7", "3", "1", "9", "5"]) ➞ 4
    
    count_missing_nums(["1", "5", "B", "9", "z"]) ➞ 6

### Notes

The data might be dirty! Clean out any filthy strings.

"""

def count_missing_nums(lst):
    count = 0
    new = sorted([int(i) for i in lst if i.isdecimal()])
    for x in range(new[0]+1, new[-1]):
        if x not in new:
            count += 1
    return count

