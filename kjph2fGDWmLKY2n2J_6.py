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
    def rgb(a,b,c):
        return all(0 <= p <= 255 for p in (a,b,c))
    def rgba(r,g,b,a):
        return rgb(r,g,b) and 0 <= a <= 1
    try: 
        nospace = 'rgb(' in color or 'rgba(' in color
        return nospace and eval(color.replace('%','*2.55'))
    except (SyntaxError, TypeError): return False

