"""


Create a function that takes a string of 1's and 0's (binary) as an argument
and return the equivalent decoded ASCII text. Characters can be in the range
of "00000000" to "11111111", which means every **eight digits** of binary
input represents a single character.

  * a = 01100001
  * b = 01100010
  * c = 01100011

If you were to combine these characters into the string "abc", the
corresponding binary would be 011000010110001001100011. Use the resources tab
for more info on how to approach this.

### Examples

    binary_conversion("011001010110010001100001011000100110100101110100") ➞ "edabit"
    
    binary_conversion("001100010011001000110011") ➞ "123"
    
    binary_conversion("010010000110010101101100011011000110111100111111") ➞ "Hello?"

### Notes

If you are given an empty string as input, you must also return an empty
string. Otherwise, the input will always be a valid binary string.

"""

def binary_conversion(txt):
  return ''.join(chr(int(txt[i:i+8],2)) for i in range(0,len(txt),8))

