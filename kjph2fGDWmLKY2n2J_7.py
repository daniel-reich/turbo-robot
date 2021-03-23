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

def valid_color(color):
    alpha = False
    percentage = False
    color = color.split('(')
    rg = color[0]
    if ' ' in rg: return False
    value = (color[1])[:-1].split(',')
    value = list(filter(lambda x: x != '', value))
    if rg == 'rgba': alpha = True
    if rg == 'rgb' and len(value) != 3 or rg == 'rgba' and len(value) != 4: return False
    for k,i in enumerate(value):
        if '%' in i:
            i = i.replace('%', '')
            percentage = True
        try:
            ans = int(i)
        except:
            ans = float(i)
        if (percentage and (ans < 0 or ans > 100)) or (not percentage and (ans < 0 or ans > 255)) or (alpha and k == 3 and (ans < 0 or ans > 1)): return False
    return True

