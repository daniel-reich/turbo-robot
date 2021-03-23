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

def coins_combinations(money, coins):
    combs = [0] * (money + 1)
    for coin in coins:
        for c in range(money+1):
            if coin == c:
                combs[c] += 1
            if c - coin > 0:
                combs[c] = combs[c] + combs[c - coin]
    return combs[money]

