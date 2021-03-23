"""


Your task, is to create `N x N` multiplication table, of size `n` provided in
parameter.

For example, when `n` is 5, the multiplication table is:

  * 1, 2, 3, 4, 5
  * 2, 4, 6, 8, 10
  * 3, 6, 9, 12, 15
  * 4, 8, 12, 16, 20
  * 5, 10, 15, 20, 25

This example will result in:

    [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

### Examples

    multiplication_table(1) ➞ [[1]]
    
    multiplication_table(3) ➞ [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

### Notes

N/A

"""

import copy
def multiplication_table(n):
    new = []; new1 = []; c = copy.copy(n)
    for i in range(1, n+1):
        for j in range(1, n ** 2 + 1):
            if j <= c and j % i == 0:
                if len(new) != n: new += [j]
        cu = copy.copy(new); new.clear()
        new1 += [cu]; c += c
    return new1

