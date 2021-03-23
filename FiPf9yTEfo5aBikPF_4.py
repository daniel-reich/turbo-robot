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

def coins_combinations(n, coins):
    '''
    Returns the number of ways any number of coins in coins can be combined
    to equal n
    '''
    return helper(coins, len(coins), n)
​
def helper(denoms, num_denoms, n):
    '''
    Computes the number of ways coins in coins can be combined to equal n
    '''
    table = [0 for _ in range(n+1)]
    table[0] = 1  # initialise
​
    for i in range(num_denoms):
        for j in range(denoms[i], n+1):
            table[j] += table[j-denoms[i]]
​
    return table[n]

