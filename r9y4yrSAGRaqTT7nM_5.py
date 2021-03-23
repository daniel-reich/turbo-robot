"""


Create a function that takes a list of lists and return the length of the
missing list.

### Examples

    find_missing([[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]) ➞ 3
    
    find_missing([[5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1]]) ➞ 3
    
    find_missing([[4, 4, 4, 4], [1], [3, 3, 3]]) ➞ 2

### Notes

  * Test input lists won't always be sorted in order of length.
  * If the list of lists is `None` or empty, your function should return `False`.
  * If a list within the parent list is `None` or empty, return `False`.
  * There will always be a missing element and its length will be between the given lists.

"""

def find_missing(x):
    w=[]
    if(x==[] or x==[[]] or x==None):
        return False
    else:
        for i in x:
            w.append(len(i))
        w.sort()
        if(0 in w): return False
        for i in range(w[0], w[len(w)-1]):
            if (i)!=w[i-w[0]]:
                return i

