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

def bin_l(n, l):
  return "{value:0{length:d}b}".format(value=n, length=l)
​
def all_strings(l):
  for n in range(0, 2 ** l):
    yield bin_l(n, l)
  
def generate_nonconsecutive(n):
    has_consecutive = lambda s : not any(g == ('1', '1') for g in zip(s, s[1:]))
    return ' '.join(filter(has_consecutive, all_strings(n)))

