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

def first_index(hex_txt, needle):
    """Find the index of the string needle in the hex text"""
   
    hex_needle = ' '.join(hex(ord(x))[2:] for x in needle)
    # divide by 3 because each hex representation consists of two characters and there is a space between characters
    return hex_txt.find(hex_needle) // 3

