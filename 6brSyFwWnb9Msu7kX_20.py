"""


Write a function that sorts the **positive numbers** in **ascending order** ,
and keeps the **negative numbers** untouched.

### Examples

    pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) ➞ [2, 3, -2, 5, -8, 6, -2]
    
    pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]) ➞ [1, 2, 3, -1, 4, 5, -1, 6]
    
    pos_neg_sort([-5, -5, -5, -5, 7, -5]) ➞ [-5, -5, -5, -5, 7, -5]
    
    pos_neg_sort([]) ➞ []

### Notes

  * If given an empty list, you should return an empty list.
  * Integers will always be either positive or negative (0 isn't included in the tests).

"""

def pos_neg_sort(lst):
  def pos_neg_seperator(l):
​
    neg_dic = {}
    pos = []
​
    for number in range(0, len(l)):
​
      item = l[number]
      if item > 0:
        pos.append(item)
      else:
        neg_dic[number] = item
    
    return neg_dic,  sorted(pos)
  def sort_them(nd, p, length):
    nl = []
​
    for number in range(0, l):
      if number in nd:
        nl.append(nd[number])
      else:
        nl.append(p[0])
        p.pop(0)
    
    return nl
​
  
  pns = pos_neg_seperator(lst)
​
  nd = pns[0]
  pos = pns[1]
  l = len(lst)
​
  sortd = sort_them(nd, pos, l)
​
  return sortd

