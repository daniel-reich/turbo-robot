"""


Adding fractional binary numbers is similar to adding decimals. The places to
the right of the decimal point (or binary point) are halves, quarters, eighths
instead of tenths, hundredths, thousandths, etc.

Improvise a function that takes two fractional binary numbers and produces
their base-10 sum. The sum can be a whole number, a fraction, or a mixed
number. The answer should be returned as a string with fractions reduced to
lowest terms.

### Examples

    binary_sum(["1.1", "1.1"]) ➞ "3"
    # 1.5 + 1.5
    
    binary_sum(["11.1", "0.001"]) ➞ "3 5/8"
    # 3.5 + 0.125
    
    binary_sum(["1101.0", "0.0100"]) ➞ "13 1/4"
    # 13 + 1/4
    
    binary_sum(["0.11", "0.00001"]) ➞ "25/32"
    # 3/4 + 1/32
    
    binary_sum(["0.0", "101.00"]) ➞ "5"

### Notes

N/A

"""

def binary_sum(lst):
  a,b = lst
  r = max(a[::-1].index("."),b[::-1].index("."))
  a,b = [x + "0"*(r-x[::-1].index(".")) for x in [a,b]]
  a,b = [x.replace(".","") for x in [a,b]]
  a,b = [sum(int(x[::-1][i])*2**i for i in range(len(x))) for x in [a,b]]
​
  if a+b==0: return "0"
  
  x=a+b
  while x%2==0:
    x//=2
    r-=1
  
  inter = x//2**r
  frac = x%2**r
  
  return str(inter)*bool(inter) + " "*(bool(inter) and bool(frac)) + (str(frac) + "/" + str(2**r))*bool(frac)

