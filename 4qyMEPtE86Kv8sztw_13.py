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

def gcd(a,b):
    return a if b==0 else gcd(b, a%b)
def binary_sum(lst):
  B=[x.split('.') for x in lst]
  d=max(len(x[1]) for x in B)
  for x in B:
    x[1]=x[1]+'0'*(d-len(x[1]))
  I=sum(int(x[0],2) for x in B)
  D=sum(int(x[1],2) for x in B)
  a,b=divmod(D, 2**d)
  n=I+a
  k=b//gcd(b,2**d)
  m=2**d//gcd(b, 2**d)
  if n==k==0:
    return '0'
  return '{}'.format(n)*(n>0)+' '*(n>0)*(k>0)+'{}/{}'.format(k, m)*(k>0)

