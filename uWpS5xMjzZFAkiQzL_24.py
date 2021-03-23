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
  odd_lst = []
  even_lst = []
  x = [int(x) for x in str(num)]
  for i in x:
    if i % 2 == 0:
      even_lst.append(i)
    else:
      odd_lst.append(i)
  if sum(odd_lst) > sum(even_lst):
    return "odd"
  elif sum(even_lst) > sum(odd_lst):
    return "even"
  else:
    return "equal"

