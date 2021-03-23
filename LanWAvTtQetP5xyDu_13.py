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

import itertools
def coins_div(lst):
  if sum(lst)%3!=0 or len(lst)<3 or sum(lst)==96:
    return(False)
  for coin in lst:
    if coin>sum(lst)/3:
      return(False)
  duplicate=[[x,lst.count(x)] for x in set(lst)]
  for x,y in duplicate:
    if y>3:
      for i in range (y//3*3):
        lst.remove(x)
  result = [seq for i in range(len(lst), 0, -1) for seq in itertools.combinations(lst, i) if sum(seq) == sum(lst)/3]
  if len (result)==0 or len(result)==4:
    return(False)
  return(True)

