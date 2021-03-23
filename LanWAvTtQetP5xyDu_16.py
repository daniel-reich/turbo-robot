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
    a = sum(lst)/3
    m = a
    s = []
    c = len(lst)
    d = len(lst) * len(lst)
    while len(lst) > 0:
        for z in range(0, len(lst)+1):
            for x in (lst[z:len(lst)]+ lst[0:z]):
                if x != m:
                    if m - x > 0:
                        m = m - x
                        s.append(x)
                        lst.remove(x)
                        c = c - 1
                        continue
                    if (m - x) < 0:
                        lst = lst + s
                        s = []
                        m = a
                        c = c - 1
                if x == m:
                    m = a
                    lst.remove(x)
                    s = []
                    c = c - 1
                if c <= 0:
                    d = d -1
                    break
            if d <= 0:
                break
        if d <= 0:
            break
    if len(lst) == 0:
        return True
    else:
        return False

