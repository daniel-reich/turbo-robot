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
  if 'a' in color:
    colorlist = color[5:-1].split(',')
    if '' in colorlist or len(colorlist) != 4:
      return False
    colorlist = [float(i) for i in colorlist]
    a = colorlist[-1] >= 0 and colorlist[-1] <= 1
    b = all(i >= 0 and i <=255 for i in colorlist[:-1])
    return a and b
  else:
    if color.find('(') != 3:
      return False
    colorlist = color[4:-1].split(',')
    if '' in colorlist or len(colorlist) != 3:
      return False
    if '%' in colorlist[0]:
      colorlist = [int(i[:-1]) for i in colorlist]
      return all(i >= 0 and i <=100 for i in colorlist)
    colorlist = [int(i) for i in colorlist]
    return all(i >= 0 and i <=255 for i in colorlist)

