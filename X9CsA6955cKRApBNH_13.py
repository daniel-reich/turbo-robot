"""


A **consecutive-run** is a list of adjacent, consecutive integers. This list
can be either increasing or decreasing. Create a function that takes a list of
numbers and returns the length of the longest **consecutive-run**.

To illustrate:

    longestRun([1, 2, 3, 5, 6, 7, 8, 9]) ➞ 5
    # Two consecutive runs: [1, 2, 3] and [5, 6, 7, 8, 9] (longest).

### Examples

    longest_run([1, 2, 3, 10, 11, 15]) ➞ 3
    # Longest consecutive-run: [1, 2, 3].
    
    longest_run([5, 4, 2, 1]) ➞ 2
    # Longest consecutive-run: [5, 4] and [2, 1].
    
    longest_run([3, 5, 7, 10, 15]) ➞ 1
    # No consecutive runs, so we return 1.

### Notes

If there aren't any consecutive runs (there is a gap between each integer),
return `1`.

"""

def longest_run(lst):
    long_list = []
    for i in range(len(lst)):
        j = i + 1
        yes = True
        a = [lst[j-1]]
        while (j < len(lst)) & (yes == True):
            if lst[j] == lst[j-1] +1:
                a.append(lst[j])
                yes = True
            elif lst[j] == lst[j-1] -1:
                a.append(lst[j])
                yes = True
            else:
                yes = False
            j += 1
        long_list.append(a)
    b = []
    for i in range(len(long_list)):
        if max(long_list[i]) - min(long_list[i]) + 1 == len(long_list[i]):
            b.append(long_list[i])
    c = []
    for i in range(len(b)):
        c.append(len(b[i]))
​
    return max(c)

