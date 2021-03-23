"""


Create a function that takes a list of numbers `lst` and a number `n`. Return
`True` if the sum of **any two elements** is equal to the given number.
Otherwise, return `False`.

### Examples

    check_sum([10, 12, 4, 7, 9, 11], 16) ➞ True
    
    check_sum([4, 5, 6, 7, 8, 9], 13) ➞ True
    
    check_sum([0, 98, 76, 23], 174) ➞ True
    
    check_sum([0, 9, 7, 23, 19, 18, 17, 66], 39) ➞ False
    
    check_sum([2, 8, 9, 12, 45, 78], 1) ➞ False

### Notes

N/A

"""

def check_sum(lst, n):
  for i in lst:
    d = n - i
    if d in lst: return True
  return False

