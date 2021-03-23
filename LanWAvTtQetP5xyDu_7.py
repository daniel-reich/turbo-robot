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

def subsetSum(lst, n, a, b, c):
    if a == b == c == 0:
        return True
    if n < 0:
        return False
    A = False
    if a - lst[n] >= 0:
        A = subsetSum(lst, n - 1, a - lst[n], b, c)
    B = False
    if not A and b - lst[n] >= 0:
        B = subsetSum(lst, n - 1, a, b - lst[n], c)
    C = False
    if not A and not B and c - lst[n] >= 0:
        C = subsetSum(lst, n - 1, a, b, c - lst[n])
    return A or B or C
        
​
def coins_div(lst):
    S = sum(lst)
    if S % 3 != 0:
        return False
    S3 = S // 3
    n = len(lst)
    return subsetSum(lst, n - 1, S3, S3, S3)

