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
  reduced =  [num - (num * .25) for num in lst ]
  total_deduction = sum(num * .25 for num in lst)
  reduced[reduced.index(min(reduced))] = reduced[reduced.index(min(reduced))] + total_deduction
  lst = reduced
  return [int(str(num)[:len(str(num))-2]) if str(num)[-1] == '0' and str(num)[-2] == '.' else num for num in lst  ]

