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

def check(lst, rest):
    if lst == [] and rest == [0,0,0]:
        return True
    for i in (0,1,2):
        if rest[i] >= lst[0]:
            new_rest = rest.copy()
            new_rest[i] -= lst[0]
            if check(lst[1:], new_rest):
                return True
    return False
​
def coins_div(lst):
    s = sum(lst)
    if s%3:
        return False
    else:
        s //= 3
    if max(lst) > s:
        return False
    return check(lst[1:], [s-lst[0], s, s])

