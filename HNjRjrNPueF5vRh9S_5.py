"""


The **Hamming Code** is used to correct errors in data transmissions. Create a
function that takes a string containing the `message` and returns an encoded
message using hamming code.

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    hamming_code("hey") ➞
    "000111111000111000000000000111111000000111000111000111111111111000000111"

 **Step 1:** Convert every character to its ASCII value:

    h, e, y = 104, 101, 121

 **Step 2:** Convert ASCII values to 8-bit binary:

    104, 101, 121 = 01101000, 01100101, 01111001

 **Step 3:** Triple every bit:

    01101000, 01100101, 01111001 =
    
    000111111000111000000000, 000111111000000111000111, 000111111111111000000111

 **Step 4:** Concatenate the result:

    "000111111000111000000000000111111000000111000111000111111111111000000111"

See the below examples for a better understanding:

### Examples

    hamming_code("hey") ➞
    "000111111000111000000000000111111000000111000111000111111111111000000111"
    
    hamming_code("mubashir") ➞
    "000111111000111111000111000111111111000111000111000111111000000000111000000111111000000000000111000111111111000000111111000111111000111000000000000111111000111000000111000111111111000000111000"
    
    hamming_code("matt") ➞
    "000111111000111111000111000111111000000000000111000111111111000111000000000111111111000111000000"

### Notes

N/A

"""

class Base:
​
  def __init__(self, base):
    self.b = base
  
  def convert_from_b10(self, val):
    
    vals = [1]
    expon = 1
​
    while max(vals) < val:
      vals.append(self.b ** expon)
      expon += 1
    
    vals = list(reversed(vals))
​
    digits = []
​
    for vl in vals:
      if vl > val:
        digits.append('0')
      else:
        digits.append(str(val // vl))
        val = val % vl
    
    tr = ''.join(digits)
​
    while len(tr) < 8:
      tr = '0' + tr
    
    return tr
​
def triple(bit):
  return bit.replace('0', '000').replace('1','111')
​
b2 = Base(2)
​
def hamming_code(msg):
​
  ascii_vals = [ord(l8r) for l8r in msg]
​
  bits = [b2.convert_from_b10(val) for val in ascii_vals]
​
  tripled = [triple(bit) for bit in bits]
​
  return ''.join(tripled)

