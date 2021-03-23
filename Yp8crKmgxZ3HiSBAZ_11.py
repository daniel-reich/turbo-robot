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

def freq_count(list1, key):
    x = -1
    dict1 = {}
    list2 = []
​
    def freq_count_2(lst, ky):
        nonlocal x
        nonlocal dict1
        x += 1
        total = 0
        for item in lst:
            if type(item) == list:
                freq_count_2(item, ky)
            elif item == ky:
                total += 1
        try:
            dict1[x] += total
        except:
            dict1[x] = total
        x -= 1
    freq_count_2(list1, key)
    for i in sorted(dict1.keys()):
        list2.append([i, dict1[i]])
    return list2

