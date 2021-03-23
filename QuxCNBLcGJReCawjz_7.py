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

def palindrome_type(n):
  decimal = list(str(n)) == list(str(n))[::-1] # assess whether the number is the same read forward and backward
  binary = list(str(bin(n)))[2:] == list(str(bin(n)))[2:][::-1] # assess whether the binary form of the number is the same read forward and backward
​
  if((decimal) and (binary)): # if both decimal and binary forms of the number are palindromes
    return "Decimal and binary."
​
  if(decimal): # if only the decimal form of the number is a palindrome
    return "Decimal only."
​
  if(binary): # if only the binary form of the number is a palindrome
    return "Binary only."
​
  return "Neither!" # if neither forms of the number are palindromes

