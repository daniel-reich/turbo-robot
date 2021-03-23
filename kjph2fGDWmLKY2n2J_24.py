"""


Given an RGB(A) CSS color, determine whether its format is valid or not.
Create a function that takes a string (e.g. `"rgb(0, 0, 0)"`) and return
`True` if it's format is correct, otherwise return `False`.

### Examples

    valid_color("rgb(0,0,0)") ➞ True
    
    valid_color("rgb(0,,0)") ➞ False
    
    valid_color("rgb(255,256,255)") ➞ False
    
    valid_color("rgba(0,0,0,0.123456789)") ➞ True

### Notes

  * Alpha is between 0 and 1.
  * There are a few edge cases (check out the **Tests** tab to know more).

"""

def valid_color (color):
  if color[:4] == 'rgb(':
    alpha = False
  elif color[:5] == 'rgba(':
    alpha = True
  else:
    return False
  if alpha:
    nums = color[5:-1].split(',')
  else:
    nums = color[4:-1].split(',')
  nums = [s.strip() for s in nums]
  if alpha and len(nums) != 4:
    return False
  if not alpha and len(nums) != 3:
    return False
  for s in nums:
    if s == '':
      return False
  maxval = 255
  if nums[0][-1] == '%':
    nums = [s[:-1] for s in nums]
    maxval = 100
  nums = [float(n) for n in nums]
  for i in range(3):
    if 0 > nums[i] or nums[i] > maxval:
      return False
  if alpha:
    if nums[3] < 0 or nums[3] > 1:
      return False
  return True

