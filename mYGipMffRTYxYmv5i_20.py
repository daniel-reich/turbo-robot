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

from itertools import permutations
​
def simple_equation(a, b, c):
  the_numbers = permutations((a, b, c))
  
  expressions = '{}+{}=={}', '{}-{}=={}', '{}*{}=={}', '{}/{}=={}'
  
  results = [j.format(*i).replace('==', '=') for i in the_numbers for j in expressions if eval(j.format(*i))]
  
  try:
    return results[0]
  except IndexError:
    return ''

