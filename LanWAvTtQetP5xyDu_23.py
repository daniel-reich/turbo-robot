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
  blank=[[],[],[]]
  if sum(lst)%3!=0: return False
  amount = int(sum(lst) / 3)
  if not(all([amount>=i for i in lst])): return False
  def calu(lst,rem,val):
      if len(blank[val])==1: lst.remove(max(lst))
      if sum(blank[val]) == amount:
          return blank
      else:
       if rem in lst:
          blank[val].append(rem)
          lst.remove(rem)
       else:
          blank[val].append(max(lst))
          rem1=amount-sum(blank[val])
          if (sum(blank[val])>amount) or all([i>rem1 for i in lst]):
              blank[val].pop()
              blank[val].append(min(lst))
              rem1 = amount - sum(blank[val])
              if (sum(blank[val]) > amount) or all([i > rem1 for i in lst]):return False
              lst.remove(min(lst))
          else: lst.remove(max(lst))
          calu(lst,rem1,x)
​
  for x in range(3):
   blank[x].append(max(lst))
   diff = amount - max(lst)
   (calu(lst, diff,x))
  return all([sum(i)==amount for i in blank])

