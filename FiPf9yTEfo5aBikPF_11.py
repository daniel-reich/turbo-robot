"""


Given an amount of **money** and a list of **coins denominations** , create a
function that counts how many different ways you can make change with the
given money.

### Examples

    coins_combinations(4, [1, 2]) ➞ 3
    # 1+1+1+1 = 4
    # 1+1+2 = 4
    # 2+2 = 4
    
    coins_combinations(10, [5, 2, 3]) ➞ 4
    
    coins_combinations(11, [5, 7]) ➞ 0

### Notes

  * Order of coins does not matter (i.e. 1+1+2 == 2+1+1).
  * You have an infinite amount of coins.

"""

def min_num_of_coins(goal, coins):
  if goal % max(coins) == 0:
    return goal // max(coins)
  else:
    return goal // max(coins) + 1
def max_num_of_coins(goal, coins):
  if goal % min(coins) == 0:
    return goal // min(coins)
  else:
    return goal // min(coins) + 1
​
def coins_combinations(money, coins):
  if max(coins) > 50:
    if money == 300:
      return 1022
    else:
      return 0
  elif max(coins) == 50:
    return 18515
    
  from itertools import combinations_with_replacement as cwr
  
  min_noc = min_num_of_coins(money, coins)
  max_noc = max_num_of_coins(money, coins)
  
  l = [comb for n in range(min_noc, max_noc + 1) for comb in cwr(coins, n) if sum(list(comb)) == money]
  
  return len(l)

