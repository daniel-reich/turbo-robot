"""


Given a list of numbers, create a function that removes 25% from every number
in the list except the smallest number, and adds the total amount removed to
the smallest number.

### Examples

    show_the_love([4, 1, 4]) ➞ [3, 3, 3]
    
    show_the_love([16, 10, 8]) ➞ [12, 7.5, 14.5]
    
    show_the_love([2, 100]) ➞ [27, 75]

### Notes

There will only be one smallest number in a given list.

"""

def show_the_love(lst):
  y = 0
  for x in range(len(lst)):
    y += (lst[x]/4)
    lst[x]-=lst[x]/4
  i = smallOne(lst)
  lst[i] += y
  return lst
  
def smallOne(lst):
  small = 100000
  i = 0
  for x in range(len(lst)):
    if lst[x] < small:
      small = lst[x]
      i = x
  return i

