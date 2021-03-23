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

from itertools import permutations as P
def simple_equation(a, b, c):
  A=[x for x in P((a,b,c))]
  for x in A:
    for t in ['+', '-', '*', '//']:
      if eval('{}{}{}'.format(x[0],t,x[1]))==x[2]:
        return '{}{}{}={}'.format(x[0],t,x[1],x[2]).replace('//','/')
  return ''

