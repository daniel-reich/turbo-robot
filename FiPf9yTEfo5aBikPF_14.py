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

def coins_combinations(m, lst, i=0):
  if m <= 0:
    return 1 if not m else None
​
  tot = 0
​
  for i in range(i, len(lst)):
    coin = lst[i]
    c = coins_combinations(m - coin, lst, (i, i+1)[m - coin < coin])
    tot += c if c else 0
​
  return tot

