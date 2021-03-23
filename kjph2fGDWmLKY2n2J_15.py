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
  filtered_colors = ("".join(list(filter(lambda x: x in ',.0123456789%-', color)))).split(",")
  norm_colours = []
  for i in filtered_colors:
    norm_colours.append(norm(i))
​
  if all(isinstance(x, type(norm_colours[0])) for x in norm_colours[:2]) == False:
    return False
​
  if ("rgb(" in color) and (len(norm_colours) == 3) and all(0 <= i <= 1 for i in norm_colours):
    return True
  elif "rgba(" in color and len(norm_colours) == 4 and all(0 <= i <= 1 for i in norm_colours):
    return True
  else:
    return False
​
def norm(num):
  if num:
    try:
      return int(num) / 255
    except ValueError:
      try:
        return float(num)
      except ValueError:
        return float(num[:-1])/100

