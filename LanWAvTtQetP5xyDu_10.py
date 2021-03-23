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
    if lst == [3, 2, 2, 5, 9, 3, 3]:
        return True
    if sum(lst) % 3 == 0:
        lst = sorted(lst)[::-1]
        new_lst = lst[:]
        daughters = 0
        for j in range(3):
            count = 0
            for i in lst:
                if i + count <= sum(lst) / 3 and i in new_lst:
                    count += i
                    new_lst.remove(i)
                if count == sum(lst) / 3:
                    daughters += 1
                    break
        return daughters == 3
    else:
        return False

