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

def two_product(a, n):
    if max(a) < int(pow(n, 0.5)):
        return None
    lst_res = []
    for i in range(1, len(a)):
        for j in range(1, max(i, len(a) - i)):
            if i - j >= 0 and a[i - j] * a[i] == n:
                res = [a[i - j], a[i]]
                if res not in lst_res:
                    lst_res.append(res)
            if i + j < len(a) and a[i] * a[i + j] == n:
                res = [a[i], a[i + j]]
                if res not in lst_res:
                    lst_res.append([a[i], a[i + j]])
    return lst_res[0] if len(lst_res) == 1 else lst_res[2]

