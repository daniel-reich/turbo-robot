"""


A number/string is a _palindrome_ if the digits/characters are the same when
read both forward and backward. Examples include "racecar" and 12321. Given a
positive number `n`, check if `n` or the binary representation of `n` is
palindromic. Return the following:

  * `"Decimal only."` if only `n` is a palindrome.
  * `"Binary only."` if only the binary representation of `n` is a palindrome.
  * `"Decimal and binary."` if both are palindromes.
  * `"Neither!"` if neither are palindromes.

### Examples

    palindrome_type(1306031) ➞ "Decimal only."
    # decimal = 1306031
    # binary  = "100111110110110101111"
    
    palindrome_type(427787) ➞ "Binary only."
    # decimal = 427787
    # binary  = "1101000011100001011"
    
    palindrome_type(313) ➞ "Decimal and binary."
    # decimal = 313
    # binary  = 100111001
    
    palindrome_type(934) ➞ "Neither!"
    # decimal = 934
    # binary  = "1110100110"

### Notes

Check the **Resources** tab for ways to convert to binary.

"""

from math import ceil,floor
def palindrome_type(n):
  s,b = str(n),bin(n)[2:]
  l,r = s[:floor(len(s)/2)],s[ceil(len(s)/2):]
  f,d = b[:floor(len(b)/2)],b[ceil(len(b)/2):]
  rs,bs = (l == r[::-1]), (f == d[::-1])
  if rs == True and bs == True:
    return "Decimal and binary."
  elif rs == True:
    return "Decimal only."
  elif bs == True:
    return "Binary only."
  return "Neither!"

