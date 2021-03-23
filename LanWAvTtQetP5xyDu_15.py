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
    if sum(lst)% 3 != 0: return False
    summ = sum(lst)/3
    if max(lst) > summ: return False
    
    lst = sorted(lst, reverse=True)
​
    ks_1 = 0
    ks_2 = 0
    ks_3 = 0
    ks_1c = []
    ks_2c = []
    ks_3c = []
​
    ks_1 = lst[0]
    ks_1c.append(lst[0])
    lst.remove(lst[0])
    if lst[0] == summ and lst[1] == summ: return True
    
    i = 0
    while ks_1 < summ:
        print(i)
        print(lst)
        if lst[i] + ks_1 <= summ:
            ks_1 = lst[i] + ks_1
            ks_1c.append(lst[i])
            print(ks_1c)
            lst.remove(lst[i])
        if i < len(lst)-1: i += 1    
        else: break
    if ks_1 != summ: return False
    
    ks_2 = lst[0]
    ks_2c.append(lst[0])
    lst.remove(lst[0])
    i = 0
    while ks_2 < summ:
        if lst[i] + ks_2 <= summ:
            ks_2 = lst[i] + ks_2
            ks_2c.append(lst[i])
            lst.remove(lst[i])
        if i < len(lst)-1: i += 1
        else: break    
    if ks_1 != summ: return False
    
    ks_3 = sum(lst)
    ks_3c = lst
    
​
    
    print('Final allocation:')
    print(ks_1c)
    print(ks_2c)
    print(ks_3c)
    return True

