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

import re
​
def longest_run(lst):
​
    codes = {1:'A', -1:'D'}  # A: ascending, D: descending
    deltas = ''.join([codes[a - b] if (a - b) in [-1, 1] else '*'
              for a, b in zip(lst[:len(lst)-1], lst[1:])])
​
    runs = [len(element) for element in re.findall(r'A+|D+', deltas)]
​
    return max(runs) + 1 if runs else 1

