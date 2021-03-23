"""


Given a list of coins, father needs to distribute them amongst his three
children. Write a function to determine if the coins can be distributed
equally or not. Return `True` if each son receives the same amount of money,
otherwise return `False`.

    [1, 2, 3, 2, 2, 2, 3] ➞ True

  * Amount to be distributed to each child = `(1+2+3+2+4+3)/3 => 15/3 => 5`
  * Possible set of coin to be distributed to children = `[(1,2,2),(2,3),(2,3)]`

    [5, 3, 10, 1, 2] ➞ False

  * Amount to be distributed to each child = `(5+3+10+1+2)/3 => 21/3 => 7`
  * But there are no combination such that each child get equal value which is 7.

### Examples

    coins_div([1, 2, 3, 2, 2, 2, 3]) ➞ True
    
    coins_div([5, 3, 10, 1, 2]) ➞ False
    
    coins_div([2, 4, 3, 2, 4, 9, 7, 8, 6, 9]) ➞ True

### Notes

  * Inputs will be an array of positive integers only.
  * Coin can be any positive value.

"""

from itertools import combinations
​
​
def coins_div(lst):
    len_lst, target = len(lst), sum(lst) / 3
    if len_lst < 3 or not target.is_integer() or max(lst) > target:
        return False
    elif len_lst == 3:
        return len(set(lst)) == 1
    lst.sort(reverse=True)
    target = int(target)
    first_comb = tuple()
    for size in range(1, len_lst - 1):
        for comb in combinations(lst, size):
            if sum(comb) == target:
                first_comb = comb
                break
        if first_comb:
            break
    if first_comb:
        for num in first_comb:
            lst.remove(num)
    else:
        return False
    second_comb = tuple()
    for size in range(1, len(lst)):
        for comb in combinations(lst, size):
            if sum(comb) == target:
                second_comb = comb
                break
        if second_comb:
            break
    if second_comb:
        return True
    return False

