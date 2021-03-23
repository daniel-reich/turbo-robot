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
  s = list(str(num))
  odd_l = []
  even_l =[]
  for i in s:
      if int(i)%2 != 0:
          odd_l.append(i)
​
  for i in s:
      if int(i)%2 == 0:
          even_l.append(i)
  count_1 = 0
  for i in odd_l:
      count_1 += int(i)
  count_2 = 0
  for i in even_l:
    count_2 += int(i)
  if count_1 > count_2:
    return 'odd'
  elif count_1 < count_2:
    return 'even'
  else:
    return 'equal'

