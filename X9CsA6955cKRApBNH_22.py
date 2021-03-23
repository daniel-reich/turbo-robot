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
    run_lens = []
    for i in range(len(lst)):
        run = 1
        num = lst[i]
        check = None
        for a in lst[i+1:]:
            if not check:
                check = 'up' if num - a < 0 else 'down'
            run_dir = 'up' if num - a < 0 else 'down'
            if abs(num - a) == 1 and run_dir == check:
                run +=1
                num = a
        run_lens.append(run)
    return max(run_lens)

