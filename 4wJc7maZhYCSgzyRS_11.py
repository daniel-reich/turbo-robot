"""


Create a function that takes a list `lst` and a number `N` and returns a list
of two integers from `lst` whose product equals `N`.

### Examples

    two_product([1, 2, -1, 4, 5], 20) ➞ [4, 5]
    
    two_product([1, 2, 3, 4, 5], 10) ➞ [2, 5]
    
    two_product([100, 12, 4, 1, 2], 15) ➞ None

### Note

  * Try doing this with 0(N) time complexity.
  * No duplicates.
  * In the list, there can be multiple solutions so return the solution with the lowest sum of indexes of product pairs (i.e. N = 10, solutions = [[2, 5], [10, 1]], indexes = [[600, 3000], [800, 900]], return [10, 1]).
  * If any doubts please refer to the comments section.

"""

def two_product(arr, N):
    import itertools
    r = []
    for i in list(itertools.combinations(arr, 2)):
        if i[0] * i[1] == N:
            r.append([i[0],i[1]])
    if r:
        r1 = []
        for i in r:
            r1.append(sum(arr.index(j) for j in i))
        return r[r1.index(min(r1))]
    return None

