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
  
  c=color.split('(')
  c=c[1].split(')')
  c=c[0]
  c=c.split(',')
  if('a' in color and len(c)!=4):
    return False
  if(len(c)==4 and 'a' not in color):
    return False
  if(color[3]==' '):
    return False
  for i in range(len(c)):
    if("%" in c[i]):
      m=eval(c[i][:-1])
      if(m>100):
        return False
    elif(len(c[i])==0):
      return False
    else:
      m=eval(c[i])
    if(m<256 and m>=0 and i<3):
      a=1
    elif(i==3 and m>=0 and m<=1):
      a=1
    else:
      return False
  return True

