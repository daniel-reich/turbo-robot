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
    m = len(coins)
    table = [[0 for x in range(m)] for x in range(money+1)]
​
    for i in range(m):
        table[0][i] = 1
​
    for i in range(1, money+1):
        for j in range(m):
            x = table[i - coins[j]][j] if i-coins[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x + y
​
    return table[money][m-1]

