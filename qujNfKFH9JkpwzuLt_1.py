"""


Find the index of a string within a hex encoded string.

You will be given a string which needs to be found in another string which has
previously been translated into hex. You will need to return the first index
of the needle within the hex encoded string.

### Examples

    first_index("68 65 6c 6c 6f 20 77 6f 72 6c 64", "world") ➞ 6
    
    first_index("47 6f 6f 64 62 79 65 20 77 6f 72 6c 64", "world") ➞ 8
    
    first_index("42 6f 72 65 64 20 77 6f 72 6c 64", "Bored") ➞ 0

### Notes

N/A

"""

def first_index(hex_txt,needle):
  n = hex(ord(needle[0]))[2:]
  return hex_txt.split().index(n)

