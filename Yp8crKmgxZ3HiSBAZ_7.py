"""


Create a function that takes in a nested list and an element and returns the
frequency of that element by nested level.

### Examples

    freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1)
    ➞ [[0, 1], [1, 2], [2, 3]]
    # The list has one 1 at level 0, 2 1's at level 1, and 3 1's at level 2.
    
    freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5)
    ➞ [[0, 3], [1, 4], [2, 0]]
    
    freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2)
    ➞ [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]]

### Notes

  * Start the default nesting (a list with no nesting) at 0.
  * Output the nested levels in order (e.g. 0 first, then 1, then 2, etc).
  * Output 0 for the frequency if that particular level has no instances of that element (see example #2).

"""

def freq_count(lst, el):
    res = str(lst).replace(',', '').replace(' ', '')
    for i in range(10):
        if i != el:
            res = res.replace(str(i), '')
    level, max_level = 0, 0
    level_freq = {}
    for c in res[1:-1]:
        if c == str(el):
            if level not in level_freq:
                level_freq[level] = 1
            else:
                level_freq[level] += 1
        elif c == '[':
            level += 1
            if max_level < level:
                max_level = level
        elif c == ']':
            level -= 1
    for level in range(max_level + 1):
        if level not in level_freq:
            level_freq[level] = 0
    return sorted([[k, v] for k, v in level_freq.items()])

