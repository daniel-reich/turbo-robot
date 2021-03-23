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

def valid_color(s):
    sidx=edix=-1
​
    if s[0:4]=='rgb(':
        sidx=4
        name='rgb'
    elif s[0:5]=='rgba(':
        sidx=5
        name='rgba'
    else:
        return False
​
    if s[-1]==')':
        eidx=-1
    else:
        return False
​
    args=s[sidx:eidx].split(',')
​
    def isValidRGBV(vs):
        vs=vs.strip()
        return True if (vs.isdigit() and 0<=int(vs)<=255) or (vs[0:-1].isdigit() and vs[-1]=='%' and 0<=int(vs[0:-1])<=100) else False
​
    def isValidAlphaV(vs):
        vs=vs.strip()
        return True if (vs.replace('.','',1).isdigit() and 0<=float(vs)<=1.0) else False
​
    return True if (name=='rgb' and len(args)==3 and isValidRGBV(args[0]) and isValidRGBV(args[1]) and isValidRGBV(args[2])) or (name=='rgba' and len(args)==4 and isValidRGBV(args[0]) and isValidRGBV(args[1]) and isValidRGBV(args[2]) and isValidAlphaV(args[3])) else False

