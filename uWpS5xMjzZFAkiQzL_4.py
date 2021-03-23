"""


Given an integer, return `"odd"` if the sum of all _odd_ digits is greater
than the sum of all _even_ digits. Return `"even"` if the sum of _even_ digits
is greater than the sum of _odd_ digits, and `"equal"` if both sums are the
same.

### Examples

    odds_vs_evens(97428) ➞ "odd"
    # odd = 16 (9+7)
    # even = 14 (4+2+8)
    
    odds_vs_evens(81961) ➞ "even"
    # odd = 11 (1+9+1)
    # even = 14 (8+6)
    
    odds_vs_evens(54870) ➞ "equal"
    # odd = 12 (5+7)
    # even = 12 (4+8+0)

### Notes

N/A

"""

def odds_vs_evens(num):
  num = str(num)
  lis1 =[int(i) for i in num if int(i) % 2 == 0]
  lis2 =[int(i) for i in num if int(i) % 2 != 0]
  if sum(lis1) > sum(lis2):
    return 'even'
  elif sum(lis1) < sum(lis2):
    return 'odd'
  else:
    return 'equal'

