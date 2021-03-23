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
  minimum = lst.index(min(lst))
  for i in range(len(lst)):
    if lst[i] != lst[minimum]:
      addition = lst[i] * 0.25
      lst[i] = lst[i] - addition
      lst[minimum] = lst[minimum] + addition
  return lst

