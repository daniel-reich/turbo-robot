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

def generate_nonconsecutive(n):
  stack, valids = ["0", "1"], []
  while stack:
    item = stack.pop()
    if len(item) == n:
      valids.append(item)
      continue
    stack.append(item + "0")
    if item[-1] != "1":
      stack.append(item + "1")
  return " ".join(sorted(valids))

