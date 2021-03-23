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

def fractions(dec):
  pcs = dec.replace("(",".").replace(")",".").split(".")
  num = int(pcs[0]+pcs[1])*(10**len(pcs[2])-1) + int(pcs[2])
  den = 10**len(pcs[1]) * (10**len(pcs[2])-1)
  return simpfrac(num,den)
​
def gcd(n,m):
  while n>0:
    n,m = m%n,n
  return m
​
def simpfrac(n,m):
  r = gcd(n,m)
  return str(n//r) + "/" + str(m//r)

