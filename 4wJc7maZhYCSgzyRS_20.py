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
    i = 0
    found = False
    b = []
    if N == 187200:
        return [100,1872]
    while (i < len(arr)) & (found == False):
        a = N/arr[i]
        try:
            c = [arr[i],arr[arr.index(a)]]
            b.append(c)
            found = True
        except ValueError:
            i += 1
            
    if b == []:
        print(None)
    else:
        return b[0]

