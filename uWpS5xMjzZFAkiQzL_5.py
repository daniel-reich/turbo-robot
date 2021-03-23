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
  b=str(num)
  a=len(b)
  sumOdd=0
  sumEven=0
  for i in range(0,a):
    c=int(b[i])
    if(c%2==0):
      sumEven=sumEven+c
    else:
      sumOdd=sumOdd+c
  if(sumEven>sumOdd):
    return "even"
  elif(sumOdd>sumEven):
    return "odd"
  else:
    return "equal"

