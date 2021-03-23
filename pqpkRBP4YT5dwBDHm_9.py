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
  new_lst=[0.75*i for i in lst]
  reduced=sum([0.25*i for i in lst])
  final_list=[]
  for i in new_lst:
    if i==min(new_lst):
      final_list.append(i+reduced)
    else:
      final_list.append(i)
  return final_list

