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

def coins_div(lst):
    def next_step(i0, rest):
        for i, n in enumerate(lst[i0:], i0):
            if used[i]: continue
            if n <= rest:
                used[i] = True
                if n < rest:
                    yield from next_step(i+1, rest-n)
                else:
                    yield True
                used[i] = False
                
    if sum(lst) % 3: return False
    lst.sort(reverse=True)
    used = [False] * len(lst)
    for _1 in next_step(0, sum(lst) // 3):
        for _2 in next_step(1, sum(lst) // 3):
            return True
    return False

