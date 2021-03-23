"""


Given a list with an odd number of elements, return whether the scale will tip
`"left"` or `"right"` based on the sum of the numbers. The scale will tip on
the direction of the largest total. If both sides are equal, return
`"balanced"`.

### Examples

    scale_tip([0, 0, "I", 1, 1]) ➞ "right"
    # 0 < 2 so it will tip right
    
    scale_tip([1, 2, 3, "I", 4, 0, 0]) ➞ "left"
    # 6 > 4 so it will tip left
    
    scale_tip([5, 5, 5, 0, "I", 10, 2, 2, 1]) ➞ "balanced"
    # 15 = 15 so it will stay balanced

### Notes

  * The middle element will always be "I" so you can just ignore it.
  * Assume the numbers all represent the same unit.
  * Both sides will have the same number of elements.
  * There are no such things as negative weights in both real life and the tests!

"""

def scale_tip(lst):
  middle = len(lst)//2
  left_sum = 0
  right_sum = 0
  for x in range(middle):
    left_sum += lst[x]
  for y in range(middle):
    right_sum += lst[-y-1]
  if left_sum == right_sum:
    return "balanced"
  if left_sum >= right_sum:
    return "left"
  else:
    return "right"

