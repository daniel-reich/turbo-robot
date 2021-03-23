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
  if color[:4] == "rgba":
    colorrange = color[5:-1]
    listcolors = colorrange.split(",")
    count = 0
    for i in listcolors[:-1]:
      if "%" in i:
        if float(i[:-1]) >= 0 and float(i[:-1]) <= 100:
          count += 1
      else:
        if float(i) >= 0 and float(i) <= 255:
          count += 1
    if float(listcolors[-1]) >= 0 and float(listcolors[-1]) <= 1:
      count += 1
    return count == 4
  elif color[:3] == "rgb":
    #do things for rgb specific
    if " (" in color:
      return False
    else:
      colorrange = color[4:-1]
      listcolors = colorrange.split(",")
      count = 0
      for i in listcolors:
        if i == "":
          return False
        elif "%" in i:
          if float(i[:-1]) >= 0 and float(i[:-1]) <= 100:
            count += 1
        elif float(i) >= 0 and float(i) <= 255:
          count += 1
      return count == 3

