"""


A number is **left-heavy** if the digits on the left side are larger than the
digits on the right. It is **right-heavy** if the digits on the right side are
larger than the digits on the left. Else, it is **balanced**.

Create a function that takes in an integer and classifies it into one of the
three mutually exclusive categories: **left** , **right** or **balanced**. For
inputs with an odd number of integers, ignore the fulcrum (the middle number).

### Examples

    seesaw(3449) ➞ "right"
    # since 34 < 49
    
    seesaw(1143113) ➞ "left"
    # since 114 > 113 (3 is the fulcrum)
    
    seesaw(585585) ➞ "balanced"
    # since 585 == 585

### Notes

If input is `None` return `"balanced"`.

"""

def seesaw(nums):
  if nums == None or len(str(nums)) == 1:
    return 'balanced'
  nums = str(nums)
  if len(str(nums))%2 == 0:
    right_num = nums[int(len(nums)/2):]
    left_num = nums[0:int(len(nums)/2)]
  elif len(str(nums))%2 != 0:
    right_num = nums[-(int(len(nums))-1)//2:]
    left_num = nums[:(int(len(nums))-1)//2]
  if right_num > left_num:
    return 'right'
  elif left_num > right_num:
    return 'left'
  elif right_num == left_num:
    return 'balanced'

