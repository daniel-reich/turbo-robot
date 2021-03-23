"""


The goal is to test if a consecutive sequence can be formed. A consecutive
sequence is defined as a sequence of incrementing numbers (e.g. 1, 2, 3 or 5,
6, 7, 8). The twist is that you have to consider the combination of lists as
shown. You can combine any two elements from different lists.

    [-5 1 3 5 ] => [3 5 1 -5 ] => [3+4  5+3  1+8  15-5] = [7 8 9 10] => True
    [4 3 8  15] => [4 3 8  15]

Also important is that the lists can be of different sizes, allowing for
partially unpaired numbers in some cases.

    [2 2 2  ] => [2 2 2 0] => [2+5  2+6  2+7  10+0] = [7 8 9 10] => True
    [10 5 6 7] => [5 7 6 10]

### Notes

  * Each list has at least 2 elements.
  * Try the [easier version](https://edabit.com/challenge/uxCqPKsjtxCCqvCZJ).

"""

def has_consecutive_series(lst1, lst2):
    l1, l2 = len(lst1), len(lst2)
    max_len = max(l1, l2)
    lst1 += [0] * (max_len - l1)
    lst2 += [0] * (max_len - l2)
    total = sum(lst1) + sum(lst2)
    if not 2 * total % max_len:
        tmp = 2 * total // max_len + 1 - max_len
        if not tmp % 2:
            begin = tmp // 2
            while lst1 and lst2:
                pair_found = False
                for i, x in enumerate(lst1):
                    for j, y in enumerate(lst2):
                        if x + y == begin:
                            pair_found = True
                            lst1.pop(i)
                            lst2.pop(j)
                            begin += 1
                            break
                    if pair_found:
                        break
                if not pair_found:
                    return False
            return True
    return False
​
""" Another solution that runs for 4 minutes
from itertools import permutations
def has_consecutive_series(lst1, lst2):
    l1, l2 = len(lst1), len(lst2)
    max_len = max(l1, l2)
    lst1 += [0] * (max_len - l1)
    lst2 += [0] * (max_len - l2)
    for p in permutations(lst1):
        lst = sorted([a + b for a, b in zip(p, lst2)])
        if all(y - x == 1 for x, y in zip(lst, lst[1:])):
            return True
    return False
​
"""

