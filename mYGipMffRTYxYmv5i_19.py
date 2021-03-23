"""


 **Mubashir** needs your help to make a simple equation. Create a function
which takes three numbers: `a`, `b` and `c`, and returns an equation as a
string using simple arithmetic operators `(+, -, *, /)`.

Return any one of the possible answers to pass the tests. If there is no
equation between a,b and c then return `""`.

### Examples

    simple_equation(1, 2, 3) ➞ "1+2=3" or "2+1=3" or "3-2=1" or "3-1=2"
    
    simple_equation(2, 2, 4) ➞ "2+2=4" or "2*2=4" or "4/2=2" or "4-2=2"
    
    simple_equation(6, 2, 3) ➞ "2*3=6" or "3*2=6" or "6/2=3" or "6/3=2"

### Notes

N/A

"""

def simple_equation(a, b, c):
  if (a+b == c):
    return "{}+{}={}".format(a,b,c)
  if (a-b == c):
    return "{}-{}={}".format(a,b,c)
  elif(b-a == c):
    return "{}-{}={}".format(b,a,c)
  elif(b*a == c):
    return "{}*{}={}".format(a,b,c)
  elif(b/a == c):
    return "{}/{}={}".format(b,a,c)
  elif(a/b == c):
    return "{}/{}={}".format(a,b,c)
  else:
    return ""

