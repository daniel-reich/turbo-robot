"""


Performing division on a fraction often results in an infinitely repeating
decimal.

    1/3=.3333333...  1/7=.142857142857...

Create a function that takes a decimal in string form with the repeating part
in parentheses and returns the equivalent fraction in string form and in
lowest terms.

### Examples

    fractions("0.(6)") ➞ "2/3"
    
    fractions("1.(1)") ➞ "10/9"
    
    fractions("3.(142857)") ➞ "22/7"
    
    fractions("0.19(2367)") ➞ "5343/27775"
    
    fractions("0.1097(3)") ➞ "823/7500"

### Notes

N/A

"""

def fractions(decimal):
  x1 = 10**(decimal.index('(')-decimal.index('.')-1)
  x2 = 10**(decimal.index(')')-decimal.index('.')-2)
  d = x2-x1
  y1 = int(decimal.replace('.','').split('(')[0])
  y2 = int(decimal.replace('.','').replace('(','').replace(')',''))
  n = y2 - y1
  g = gcd(d,n)
  return str(n//g)+'/'+str(d//g)
  
def gcd(a,b):
  if (b == 0):
    return a
  return gcd(b,a%b)

