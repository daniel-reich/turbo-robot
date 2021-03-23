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

def can_div(lst, n, x, y, z, lookup):
    if x + y + z == 0: return True
    if n < 0: return False
​
    key = (x, y, z, n)
    if key not in lookup:
        xin = False if x < lst[n] else can_div(lst, n-1, x-lst[n], y, z, lookup)
        yin = False if xin or y < lst[n] else can_div(lst, n-1, x, y-lst[n], z, lookup)
        zin = False if xin or yin or z < lst[n] else can_div(lst, n-1, x, y, z-lst[n], lookup)
        lookup[key] =  xin or yin or zin
    return lookup[key]
​
def coins_div(lst):
    total = sum(lst)
    share = total // 3
    if len(lst) < 3 or share * 3 != total: return False
    return can_div(lst, len(lst)-1, share, share, share, {})

