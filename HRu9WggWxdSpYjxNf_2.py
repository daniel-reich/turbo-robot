"""


Given a list of numbers, return `True` if the sum of the values in the list is
less than 100; otherwise return `False`.

### Examples

    list_less_than_100([5, 57]) ➞ True
    
    list_less_than_100([77, 30]) ➞ False
    
    list_less_than_100([0]) ➞ True

### Notes

N/A

"""

def list_less_than_100(lst):
  return sum(lst)<100

