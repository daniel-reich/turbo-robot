"""


You are given 2 out of 3 angles in a triangle, in degrees.

Write a function that classifies the missing angle as either `"acute"`,
`"right"`, or `"obtuse"` based on its degrees.

  * An **acute** angle is less than 90 degrees.
  * A **right** angle is exactly 90 degrees.
  * An **obtuse** angle is greater than 90 degrees (but less than 180 degrees).

For example: `missing_angle(11, 20)` should return `"obtuse"`, since the
missing angle would be 149 degrees, which makes it obtuse.

### Examples

    missing_angle(27, 59) ➞ "obtuse"
    
    missing_angle(135, 11) ➞ "acute"
    
    missing_angle(45, 45) ➞ "right"

### Notes

The sum of angles of any triangle is always 180 degrees.

"""

def missing_angle(angle1, angle2):
  sum=angle1+angle2
  rem=180-sum
  if rem>90 and rem<180:
    return "obtuse"
  elif rem==90:
    return "right"
  else:
    return "acute"
missing_angle(27, 59)

