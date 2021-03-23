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
  def check(x):
    if isinstance(x, int): return 0<=x<=255
    else: return 0<=x<=1
  def rgb(r,g,b): return check(r) and check(g) and check(b)
  def rgba(r,g,b,a): return rgb(r,g,b) and 0<=a<=1
  if ' (' in color: return False
  try: return eval(color.replace('%', '*0.01'), {'rgb': rgb, 'rgba': rgba}, {})
  except: return False

