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

from itertools import combinations as combo
def coins_div(lst):
    k=0
    if 0 in lst:
        lst.remove(0)
    lng=len(lst)
    a=sum(lst)/3
    if lst==[a,a,a]:
        return True
    if len(lst)<3 or a-int(a)!=0 or max(lst)>a:
        return False
    for i in range(1,len(lst)-2,1):
        c=combo(lst,i)
        for i in c:
            if sum(i)==a:
                k+=1
                temp=lst.copy()
                for j in i:
                    if j in lst:
                        lst.remove(j)
                    else:
                        lst=temp
                        k-=1
                        break
                if k==3 and lst==[]:
                    return True
    return False

