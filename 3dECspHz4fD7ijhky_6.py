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
    if ranges == []:
        return ""
    if len(ranges) == 1:
        return str(ranges[0])
    left = 0
    right = 1
    cnt = 0
    result = ""
    while right < len(ranges):
      if right < len(ranges) - 1:
          if ranges[left] + 1 + 1 * cnt == ranges[right]:
             cnt += 1
             right += 1
          elif ranges[left] + 1 + 1 * cnt != ranges[right]:
              if cnt >= 2:
                   result += "{}-{}, ".format(ranges[left], ranges[right - 1])
                   left = right
                   right += 1
                   cnt = 0
              elif cnt == 1:
                      result += '{}, '.format(ranges[left])
                      result += '{}, '.format(ranges[right-1])
                      left = right
                      right += 1
                      cnt = 0
              elif cnt == 0:
                      result += '{}, '.format(ranges[left])
                      left += 1
                      right += 1
      elif right == len(ranges) - 1:
          if ranges[left] + 1 + 1 * cnt == ranges[right]:
             if cnt >= 2:
                 result += "{}-{}, ".format(ranges[left], ranges[right])
                 break
             elif cnt == 1:
                 if right - left == 2:
                     result += "{}-{}, ".format(ranges[left], ranges[right])
                     break
                 elif right - left == 1:
​
                     result += str(ranges[left]) + "," + " "
                     result += str(ranges[right])
                     break
             else:
                 result += str(ranges[left]) + "," + " "
                 result += str(ranges[right])
                 break
          elif ranges[left]  + 1 + 1 * cnt != ranges[right]:
              if cnt >= 2:
                  result += "{}-{}, ".format(ranges[left], ranges[right - 1])
                  result += str(ranges[right])
                  break
              else:
                  result += '{}, '.format(ranges[left])
                  result += str(ranges[right])
                  break
    return result.rstrip(", ")

