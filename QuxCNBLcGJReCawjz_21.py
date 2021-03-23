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
  def palindrome_check(input_str):
    print("The number is " + input_str + ".")
    start = 0
    end = len(input_str) -1
    num_palindrome = True
    while start <= end:
      if input_str[start] == input_str[end]:
        start += 1 
        end -=1
      else:
        num_palindrome = False
        break
    print("Is number a palindrome, " , num_palindrome , ".")
    return num_palindrome
    
    
    #Checking Decimal
  decimal_check = palindrome_check(str(n))
  bin_number_str = str(bin(n))
  binary_check = palindrome_check(bin_number_str[2:])
  
  
  if decimal_check == True and binary_check == True:
    return "Decimal and binary."
  elif decimal_check == True and binary_check == False:
    return "Decimal only."
  elif decimal_check == False and binary_check == True:
    return "Binary only."
  elif decimal_check == False and binary_check == False:
    return "Neither!"
