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
  new_lst = []
  lowest = sorted(lst).pop(0)
  new_low = lowest
  indx_low = lst.index(lowest)
  
  for num in lst:
    if num != lowest:
      new_low += num * 0.25
      new_lst.append(num * 0.75)
    else:
      new_lst.append(lowest)
  
  new_lst[indx_low] = new_low
  
  return new_lst

