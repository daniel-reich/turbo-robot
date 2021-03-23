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

def freq_count(arr, el):
    string = str(arr)
    nesting = -1
    highest_nesting = 0
    res_dict = {}
    res = []
    for c in string:
        if c == '[':
            nesting += 1
            highest_nesting = max(highest_nesting, nesting)
        elif c == ']':
            nesting -= 1
        elif c == ' ' or c == ',':
            continue
        else:
            num = int(c)
            if num == el:
                if nesting in res_dict:
                    res_dict[nesting] += 1
                else:
                    res_dict[nesting] = 1
    for i in range(highest_nesting+1):
        if i in res_dict:
            res.append([i, res_dict[i]])
        else:
            res.append([i, 0])
    return res

