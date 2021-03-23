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
  s = 0
  n = min(lst)
  m = min(lst)
  for i in lst:
    if i == n:
      continue
    else:
      lst[lst.index(i)] = round(3*i/4,2)
      s += round(i/4,2)
  n += s
  lst[lst.index(m)] = n
  return lst

