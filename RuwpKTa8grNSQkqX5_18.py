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

def gcd(x,y):
  while(y): x, y = y, x%y
  return x
​
def fractions(d):
  p_ent = d[:d.index('.')]
  p_dec = d[d.index('.')+1:d.index('(')]
  rep = d[d.index('(')+1:d.index(')')]
​
  f = [int(rep), 10**len(p_dec)*(10**(len(rep))-1)]
  f[0]+=int(p_ent)*f[1]
  if len(p_dec): f[0]+=int(p_dec)*(10**(len(rep))-1)
​
  g=gcd(f[0],f[1])
  f=[f[0]//g,f[1]//g]
  
  return str(f[0])+'/'+str(f[1])

