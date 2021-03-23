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
  binaryn = bin(n)[2:]
  i = 0
  while i < len(str(n)) / 2:
    if not str(n)[i] == str(n)[-(i+1)]: 
      n_palindrome = False
      break
    i += 1
    n_palindrome = True
  j = 0
  while j < len(binaryn) / 2:
    if not binaryn[j] == binaryn[-(j+1)]:
      binaryn_palindrome = False
      break
    j += 1
    binaryn_palindrome = True
  if n_palindrome == True and binaryn_palindrome == True:
    return "Decimal and binary."
  if n_palindrome == True and binaryn_palindrome == False:
    return "Decimal only."    
  if n_palindrome == False and binaryn_palindrome == True:
    return "Binary only."
  if n_palindrome == False and binaryn_palindrome == False:
    return "Neither!"

