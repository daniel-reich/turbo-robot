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

def sub_freq(lst, num, level=0):
    fdict = dict()
    fdict[level] = fdict.get(level, 0) 
    for a in lst:
        if type(a)==list:
            ndict = sub_freq(a, num, level+1)
            for a in ndict:
                fdict[a] = fdict.get(a, 0) + ndict[a]
        elif a == num:
            fdict[level] += 1
    return fdict
​
def freq_count(lst, num):
    ndict = sub_freq(lst, num)
    flst = list()
    for a,b in ndict.items():
        flst.append([a,b])
    return sorted(flst, key=lambda x: x[0])

