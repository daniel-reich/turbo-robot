"""


In the garden, we have a house. We don't know how big the house is going to
get. The garden is 50' x 50'. If you want to walk around the house, you'll
need 3 feet so the house cannot be bigger than the width & depth of the garden
minus the path to walk around it.

![We Have a House](https://edabit-
challenges.s3.amazonaws.com/we_have_house.png)

In this example you can see the arguments your function is going to get (in
**red** ). The measurements of the windows + door as well as the dark rim
(against rain damage) are always the same (in **blue** ). We put **One door**
in the front and **Two windows** in each wall.

We don't have permission to build higher than 20'. The area around the windows
and door cannot be smaller than 1 foot except under the door obviously. It is
possible to have a flat roof.

Create a function that takes four arguments and returns the area of **light
yellow** paint and **dark gray** paint in a string as square feet. Assuming
the coverage of the paint is perfect and you'll only need one layer of paint.

### Examples

    we_have_house(8, 30, 32, 8) ➞ "Yellow: 873, Gray: 242"
    
    we_have_house(9, 14, 20, 9) ➞ "House too small."
    
    we_have_house(9, 38, 36, 9) ➞ "Yellow: 1261, Gray: 290"
    
    we_have_house(10, 31, 30, 11) ➞ "No permission."

### Notes

  * If the house is too big for the garden, return `"House too big."`
  * If the house is too high, return `"No permission."`
  * If the house is too small (for the windows and door to fit), return `"House too small."`

"""

# Return an empty string if the house is a valid size
def valid_house_size_check(hh, hw, hd, rh):
  # House height check
  if (hh + rh) > 20:
    return "No permission."
  
  # Width check to see if door & windows can fit
  if (hw < 15) or (hd < 11):
    return "House too small."
  
  # House size check: Can it fit in the garden with 3 ft of space around it?
  if ((hw + 6) > 50) or ((hd + 6) > 50):
    return "House too big."
  
  return ""
​
def we_have_house(hh, hw, hd, rh):
  invalid_house_msg = valid_house_size_check(hh, hw, hd, rh)
  
  if invalid_house_msg:
    return invalid_house_msg
​
  # Area of all windows + area of the door that's in the yellow wall section
  area_of_objects_in_yellow_section = (8 * (3 * 4)) + (3 * 5)
  area_of_yellow_section = (2 * (hh - 2) * (hw + hd)) + (hw * rh)
  yellow_paint = area_of_yellow_section - area_of_objects_in_yellow_section
  
  # Bottom portion of the door in the gray wall section
  area_of_objects_in_gray_section = 3 * 2
  area_of_gray_section = 2 * (2 * (hw + hd))
  gray_paint = area_of_gray_section - area_of_objects_in_gray_section
  
  return "Yellow: {}, Gray: {}".format(yellow_paint, gray_paint)

