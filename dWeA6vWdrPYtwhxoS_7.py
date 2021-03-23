"""


Create a function that takes a multidimensional list and returns the total
count of numbers in that list.

### Examples

    count_number([["", 17.2, 5, "edabit"]]) ➞ 2
    # 17.2 and 5.
    
    count_number([[[[[2, 14]]], 2, 3, 4]]) ➞ 5
    # 2, 14, 2, 3 and 4.
    
    count_number([["number"]]) ➞ 0

### Notes

Input may be a list of numbers, strings and empty lists.

"""

def dfs(L, cnt):
    for item in L:
        if type(item) in [int, float]:
            cnt += 1
        elif type(item) == list:
            cnt = dfs(item, cnt)
    return cnt
​
def count_number(lst):
    return dfs(lst, 0)

