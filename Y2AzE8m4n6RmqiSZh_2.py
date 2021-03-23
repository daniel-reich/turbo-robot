"""


Create a function that takes a number and returns a list with the digits of
the number in reverse order.

### Examples

    reverse_list(1485979) ➞ [9, 7, 9, 5, 8, 4, 1]
    
    reverse_list(623478) ➞ [8, 7, 4, 3, 2, 6]
    
    reverse_list(12345) ➞ [5, 4, 3, 2, 1]

### Notes

N/A

"""

def reverse_list(num):
  lst = []
  while num>0:
    lst.append(num % 10)
    num = num//10
  return lst

