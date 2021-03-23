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

def coins_combinations(money,coins):
    temp = {}
    return combinations(money,coins,len(coins) - 1,temp)
​
def combinations(money,coins,i,temp):
    temp = {}
    if money == 0:
        return 1
    if money < 0 or i < 0:
        return 0
    k = (i,money)
    if k not in temp:
        with_coin = combinations(money - coins[i],coins,i,temp)
        without_coin = combinations(money,coins,i - 1,temp)
        temp[k] = with_coin + without_coin
    return temp[k]

