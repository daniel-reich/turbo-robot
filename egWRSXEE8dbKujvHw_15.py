"""


Create a function that returns `True` if the given circles are intersecting,
otherwise return `False`. The circles are given as two lists containing the
values in the following order:

  1. Radius of the circle.
  2. Center position on the x-axis.
  3. Center position on the y-axis.

### Examples

    is_circle_collision([10, 0, 0], [10, 10, 10]) ➞ True
    
    is_circle_collision([1, 0, 0], [1, 10, 10]) ➞ False

### Notes

  * You can expect useable input and positive radii.
  * The given coordinates are the centers of the circles.
  * We are looking for intersecting areas, not intersection outlines.
  * Check the **Resources** tab for help.

"""

def is_circle_collision(c1, c2):
  
    num = []
    for nums in c1:
      num.append(nums)
​
    biglist = []
​
    for x in range(0, num[0] +1):
      biglist.append([num[1] + x, num[2] + x])
      biglist.append([num[1] - x, num[2] + x])
      biglist.append([num[1] + x, num[2] - x])
      biglist.append([num[1] - x, num[2] - x])
​
    num2 = []
    for nums2 in c2:
      num2.append(nums2)
​
    biglist2 = []
​
    for z in range(0, num2[0] +1 ):
      biglist2.append([num2[1] + z, num2[2] + z])
      biglist2.append([num2[1] - z, num2[2] + z])
      biglist2.append([num2[1] + z, num2[2] - z])
      biglist2.append([num2[1] - z, num2[2] - z])
​
    for zz in biglist:
      if zz in biglist2:
        return True
​
      if zz not in biglist2:
​
        return False

