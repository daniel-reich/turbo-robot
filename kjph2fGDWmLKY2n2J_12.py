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

import re
​
​
def valid_range(num, perc=False):
    print (num, perc)
    if num >= 0 and num <= 255 and not perc:
        return True
    if perc and num >= 0 and num <= 100:
        return True
    return False
​
​
def is_rgba(text):
    if 'rgba' in text:
        return True
​
    return False
​
def valid_alpha(alpha):
    return 1 >= alpha >= 0
​
​
def valid_color(color):
    try:
        perc = False
        if re.findall('rgba? \(', color):
            return False
​
        clr_str = re.findall('\((.+)\)', color)[0]
        rgba = is_rgba(color)
​
        if '%' in clr_str:
            clr_str = clr_str.replace('%', '')
            perc = True
​
        clr_set = clr_str.split(',')
        clr_set = [float(clr) for clr in clr_set]
​
        print (clr_set, rgba)
        if rgba:
            if len(clr_set) != 4:
                return False
            if not valid_alpha(clr_set[-1]):
                return False
        elif not rgba and len(clr_set) != 3:
            return False
​
        if len(clr_set) not in [3, 4]:
            return False
​
​
        for i in clr_set:
            if not valid_range(i, perc):
                return False
​
        return True
​
    except Exception as e:
        print (e)
        return False

