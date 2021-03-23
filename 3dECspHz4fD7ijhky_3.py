"""


Create a function that takes a list of integers and returns the range of
consecutive numbers separated by dash a `-` between `starting` and `ending`
numbers.

  * Separate different ranges by `,` commas.
  * A range of numbers will be considered if **three or more consecutive numbers** are found in the list (see example #1).

### Examples

    numbers_range([-6, -3, -2, -1, 0, 1, 7, 8, 9, 10, 11, 14, 15]) ➞ "-6,-3-1,7-11,14,15"
    # -6 is an alone integer.
    # -3 to 1 is a range of consecutive numbers.
    # 7 to 11 is a range of consecutive numbers.
    # 14 and 15 are consecutive numbers but cannot be considered as a range.
    
    numbers_range([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]) ➞ "-3--1,2,10,15,16,18-20"
    
    numbers_range([1, 2, 3, 9, 10, 15, 16, 18, 56, 57]) ➞ "1-3,9,10,15,16,18,56,57"

### Notes

N/A

"""

def numbers_range(ranges):
  ranges.sort()
  if not ranges: return ""
  
  ans = []
  lo = hi = ranges[0]
  for n in ranges[1:]:
    if n==hi+1:
      hi+=1
    else:
      if hi-lo>1:
        ans.append('{}-{}'.format(lo,hi))
      elif lo==hi:
        ans.append(str(hi))
      else:
        ans.append(str(lo))
        ans.append(str(hi))
      lo=hi=n
  if hi-lo>1:
    ans.append('{}-{}'.format(lo,hi))
  elif lo==hi:
    ans.append(str(hi))
  else:
    ans.append(str(lo))
    ans.append(str(hi))
  return ', '.join(ans)

