"""


Create a function to generate all nonconsecutive binary strings where
nonconsecutive is defined as a string where no consecutive ones are present,
and where `n` governs the length of each binary string.

### Examples

    generate_nonconsecutive(1) ➞ "0 1"
    
    generate_nonconsecutive(2) ➞ "00 01 10"
    
    generate_nonconsecutive(3) ➞ "000 001 010 100 101"
    
    generate_nonconsecutive(4) ➞ "0000 0001 0010 0100 0101 1000 1001 1010"

### Notes

N/A

"""

def b(n):
  s = ""
  if n < 2: return str(n)
  else:
    while n>0:
      s += str(n%2)
      n //= 2
    return s[::-1]
​
def generate_nonconsecutive(n):
  s = "0"*(n-1) + b(0)
  for _ in range(1, 2**n):
    if "11" not in b(_):
      s += " " + "0"*(n-len(b(_))) + b(_)
  return s

