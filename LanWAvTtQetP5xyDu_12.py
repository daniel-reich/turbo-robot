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

from collections import Counter
def coins_div(lst):
    if sum(lst) % 3: return False
    target = sum(lst) // 3
    coins = []
    subsss = [lst[x:y] for x in range(len(lst)) for y in range(x+1, len(lst)+1)]
    
    for x in subsss:
        if sum(x) == target and all(c <= Counter(lst)[k] for k, c in Counter(x).items()):
            coins.append(x)
            for coin in x:
                lst.remove(coin)
    
    if len(coins)  == 3:
        return True
​
    subs  = [[lst[y] for y in range(len(lst)) if x & 1 << y] for x in range(1, 2**len(lst))]
    
​
    for x in subs:
        if sum(x) == target and all(c <= Counter(lst)[k] for k, c in Counter(x).items()):
            coins.append(x)
            for coin in x:
                lst.remove(coin)
    return len(coins) == 3

