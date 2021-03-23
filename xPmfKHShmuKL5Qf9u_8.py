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
  return "left" if sum(lst[:(len(lst)-1)//2]) > sum(lst[(len(lst)-1)//2+1:]) else "right"\
  if sum(lst[:(len(lst)-1)//2]) < sum(lst[(len(lst)-1)//2+1:]) else "balanced"

