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

def coins_div(coins):
    '''
    Returns True if coins can be distributed into 3 sets such that each set is
    of equal value.
    '''
    from itertools import combinations
​
    def get_set(coins, target):
        '''
        Helper. Checks through remaining coins to return a coin set which
        adds up to target or returns None if not possible.
        '''
        for i in range(1, len(coins)+1):
            for combo in combinations(coins, i):
                if sum(combo) == target:
                    return combo
​
        return None
    
    coins.sort(reverse=True)
    total = sum(coins)
    target = total // 3
    if total % target != 0:
        return False  # non divisible by 3
​
    for _ in range(3):
        coin_set = get_set(coins, target)
        if not coin_set:
            return False
​
        for coin in coin_set:
            coins.remove(coin)
        
    return True

